# run uvicorn in the background from the shell script with poetry run
OPENAI_API_KEY=1337 poetry run uvicorn app:app --host 0.0.0.0 &
FOO_PID=$!
echo $FOO_PID 

cd frontend && npm start
kill $FOO_PID