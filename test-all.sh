for TEST_FILE in ./test-*.py
do
    echo "BENCHMARK ${TEST_FILE}"
    time python ${TEST_FILE}
    echo ""
done