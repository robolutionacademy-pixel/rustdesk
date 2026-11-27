"""Read-only branding preflight; does not compile, install or connect."""
from pathlib import Path
import struct
import xml.etree.ElementTree as ET
import zlib

ROOT = Path(__file__).resolve().parents[1]
ANDROID = ROOT / "flutter/android/app/src/main"
WIN = ROOT / "flutter/windows/runner"
NS = "{http://schemas.android.com/apk/res/android}"

def check_png(data):
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    offset = 8
    chunks = []
    while offset < len(data):
        length = struct.unpack_from(">I", data, offset)[0]
        name = data[offset+4:offset+8]
        end = offset+8+length
        assert end+4 <= len(data)
        payload = data[offset+8:end]
        assert zlib.crc32(name+payload) == struct.unpack_from(">I", data, end)[0]
        chunks.append(name)
        if name == b"IHDR":
            assert struct.unpack_from(">II", payload) == (128,128)
        offset = end+4
    assert chunks[0] == b"IHDR" and chunks[-1] == b"IEND"
    assert b"IDAT" in chunks

def main():
    manifest = ET.parse(ANDROID / "AndroidManifest.xml").getroot()
    app = manifest.find("application")
    assert app is not None
    assert app.attrib[NS+"label"] == "RoboDesk"
    assert app.attrib[NS+"icon"] == "@drawable/robodesk_launcher"
    assert any(s.attrib.get(NS+"label") == "RoboDesk Input" for s in app.findall("service"))
    png = (ANDROID / "res/drawable-nodpi/robodesk_launcher.png").read_bytes()
    check_png(png)
    ico = (WIN / "resources/app_icon.ico").read_bytes()
    assert struct.unpack_from("<HHH", ico) == (0,1,1)
    assert ico[6:8] == bytes((128,128))
    length, offset = struct.unpack_from("<II", ico, 14)
    assert offset == 22 and length == len(png) and ico[offset:] == png
    rc = (WIN / "Runner.rc").read_text(encoding="utf-8-sig")
    for item in ('"RoboDesk Remote Desktop"', '"ProductName", "RoboDesk"', '"CompanyName", "Robolution Technologies Ltd."'):
        assert item in rc, item
    assert (ROOT / "LICENSE").is_file(), "Preserve upstream license"
    print("Branding preflight passed. Not a build, security test or release.")

if __name__ == "__main__":
    main()
