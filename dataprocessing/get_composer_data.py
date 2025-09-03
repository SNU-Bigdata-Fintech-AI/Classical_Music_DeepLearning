import json
import re
import shutil
from pathlib import Path


META_JSON = '../aria-midi-v1-unique-ext/metadata.json'
COMPOSER = 'chopin'  # 추출할 작곡가
SRC_PATH = '../aria-midi-v1-unique-ext/data'
DST_PATH = '../aria-midi-v1-unique-ext/filtered_mid_' + COMPOSER

# 6자리 ID로 정규화
def normalize_ids(ids):
    """ids: {'4','36','103'} 혹은 {4,36,103} 등 -> {'000004','000036','000103'}"""
    norm = set()
    for x in ids:
        s = str(x)
        m = re.match(r'^(\d{1,6})', s)
        if m:
            norm.add(m.group(1).zfill(6))
    return norm

# (선택) metadata.json에서 특정 작곡가 ID 뽑기 + 6자리 패딩
def load_ids_from_metadata(metadata_path, composer='chopin'):
    with open(metadata_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    raw_ids = {k for k, v in data.items() if v.get("metadata", {}).get("composer") == composer}
    return normalize_ids(raw_ids)

# 파일명 패턴: 6자리ID_0.mid 에서 6자리 ID 추출
ID_PATTERN = re.compile(r'^(\d{6})_0\.mid$')

def collect_mid_by_ids(source_root, dest_dir, target_ids_6):
    """
    source_root: 'aria-midi-v1-unique-ext/data' 루트
    dest_dir   : 선별된 .mid를 모을 폴더 (평탄화하여 복사)
    target_ids_6: {'000004','000036', ...} 형태의 6자리 문자열 ID 집합
    """
    source_root = Path(source_root)
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    copied = 0
    for path in source_root.rglob('*.mid'):
        name = path.name
        m = ID_PATTERN.match(name)
        if not m:
            continue  # 형식이 XXXXXX_0.mid가 아니면 스킵
        fid6 = m.group(1)  # 6자리 ID
        if fid6 in target_ids_6:
            # 충돌 방지: 원래 상대 경로를 접두로 붙여 저장
            rel = path.relative_to(source_root)
            safe_parent = rel.parent.as_posix().replace('/', '__')
            out_name = f"{fid6}__{safe_parent}__{name}" if safe_parent != '.' else f"{fid6}__{name}"
            shutil.copy2(path, dest_dir / out_name)
            copied += 1

    print(f"[DONE] Copied {copied} files to: {dest_dir.as_posix()}")


if __name__ == "__main__":
    chopin_ids = load_ids_from_metadata(META_JSON, composer = COMPOSER)
    collect_mid_by_ids(
        source_root=SRC_PATH,
        dest_dir=DST_PATH,
        target_ids_6=chopin_ids
    )