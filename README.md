# django-cicd-server

### 1. settings ip 추가하기!!

8:20

## 비밀정보 설정

운영에 사용한 SECRET_KEY와 DB 비밀번호는 새 값으로 교체하세요.
Git 기록을 정리해도 포크 원본이나 기존 복제본의 값은 회수되지 않습니다.

1. 저장소 루트에서 `.env.example`을 `.env`로 복사합니다.
2. `DJANGO_SECRET_KEY`와 `DB_PASSWORD`에 서로 다른 새 난수를 넣습니다.
   예: `python -c "import secrets; print(secrets.token_urlsafe(64))"`
3. Docker Compose는 로컬 `.env`를 읽고 필요한 값을 컨테이너에 전달합니다.
   Django를 직접 실행할 때는 두 값을 해당 프로세스의 환경변수로 지정해야 합니다.
4. 기존 PostgreSQL 데이터가 있다면 `.env` 수정만으로 DB 비밀번호가 변경되지 않습니다.
   DB 관리 도구에서 실제 계정의 비밀번호도 변경한 뒤 애플리케이션을 재배포하세요.

`.env`와 DB 데이터는 Git 및 Docker 이미지 빌드에서 제외됩니다.
키를 GitHub Actions Secrets에 등록하는 것만으로 원격 서버에 자동 전달되지는 않습니다.
원격 배포 서버에도 별도로 환경변수를 준비하세요. 노출된 이전 Django 키는 운영용
SECRET_KEY_FALLBACKS에 남기지 마세요.

## 기록 정리 이후 배포

기록이 재작성되었으므로 기존 배포 서버의 checkout에서 바로 `git pull`로 합치지 마세요.
서버의 `.env`와 데이터 디렉터리를 안전하게 백업하고, 정리된 저장소를 새 경로에 clone한 뒤
환경변수와 데이터를 연결하여 배포하세요. 이번 정리 커밋은 `[skip ci]`로 자동 배포를 건너뜁니다.
CI 테스트에서는 임시 난수를 사용하며 운영 비밀정보를 사용하지 않습니다.

