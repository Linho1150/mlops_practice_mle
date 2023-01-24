# Postgres를 docker-compose로 실행하기

> pywintypes.error: (2, 'CreateFile', '지정된 파일을 찾을 수 없습니다.')

Docker를 실행하지 않아서 발생하는 오류였다.

# Docker-compose가 .env를 인식하지 않는 오류

> postgres-server | [225] FATAL: role "myuser" does not exist

.env에 USER=myuser로 설정했음에도 불구하고 인식이 안되는 문제가 있었다.
원인는 `docker-compose config`를 통해 알 수 있었는데 환경변수 USER가 myuser가 아닌 컴퓨터 이름으로 인식되어있었다.
따라서 .env는 리눅스 환경변수로 사용될만한 내용은 제외해야한다.

# Module을 찾지 못하는 문제

> data-generator | ModuleNotFoundError: No module named 'database.mlops_query_manager'

위와 같은 오류가 발생하여 문제를 찾아본 결과 패키지명을 인식하지 못했을 가능성이 있다.
방법이 여러가지 있는데 1. sys.path에 경로를 추가하거나 2. PYTHONPATH 환경변수를 추가하거나 3. **init**.py 가 존재하는지 확인하는 것이다.
3번은 사전에 세팅이 완료되어 2번 작업으로 진행하였고 아래와 같은 코드를 Dockerfile내에 추가하였다.

```
WORKDIR /usr/app
COPY . /usr/app

ENV PYTHONPATH /usr/app
```

환경변수에 프로젝트가 존재하는 파일 경로를 추가해주었다. 또한 COPY에서 선별적으로 파일을 옮기는 것이 아닌 프로젝트 폴더 전체를 옮겨버렸다.

# Docker-compose에서 Python으로 Database 접근시

```
data-generator   | Traceback (most recent call last):
data-generator   |   File "/usr/app/database/mlops_repository.py", line 9, in __init__
data-generator   |     self.db_connect= psycopg2.connect(
data-generator   |   File "/usr/local/lib/python3.9/site-packages/psycopg2/__init__.py", line 122, in connect
data-generator   |     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
data-generator   | psycopg2.OperationalError: connection to server at "0.0.0.0", port 5432 failed: Connection refused
data-generator   |      Is the server running on that host and accepting TCP/IP connections?
```

psycopg2를 활용하여 DB를 접속하는 과정에서 위와 문제를 직면하였다.
Host를 localhost나 0.0.0.0으로 설정해서 발생하는 문제였는데, host를 컨테이너 명으로 정확하게 기입하니까 연결에 성공하였다.

> localhost -> postgresql-server

이유는 조금더 리서치가 필요할 것으로 보인다.
