import os
import shutil
import sys
import logging

BASE_SOURCE_PATH = r"C:\\"   # 소스 루트
BASE_TARGET_PATH = r"C:\\"   # 타겟 루트

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "migrate.log")
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

def migrate_one(source_code: str, target_code: str):
    source_prefix = source_code[:4]
    target_prefix = target_code[:4]

    source_dir = os.path.join(
        BASE_SOURCE_PATH,
        source_prefix,
        source_code
    )

    target_prefix_dir = os.path.join(
        BASE_TARGET_PATH,
        target_prefix
    )

    target_dir = os.path.join(
        target_prefix_dir,
        target_code
    )

    if not os.path.exists(source_dir):
        msg = f"[SKIP] 소스 없음: {source_dir}"
        print(msg)
        logging.warning(msg)
        return

    # 사본 폴더가 이미 존재할 때
    if os.path.exists(target_dir): # 패쓰
        print(f"[SKIP] 이미 존재: {target_dir}")
        return
    # if os.path.exists(target_dir): # 덮어쓰기
        # shutil.rmtree(target_dir)

    os.makedirs(target_prefix_dir, exist_ok=True)

    shutil.copytree(source_dir, target_dir)

    print(f"[OK] {source_code} → {target_code}")


def main():
    for line in sys.stdin:
        line = line.strip()

        if not line or "," not in line:
            continue

        source_code, target_code = map(str.strip, line.split(",", 1))
        migrate_one(source_code, target_code)


if __name__ == "__main__":
    main()
