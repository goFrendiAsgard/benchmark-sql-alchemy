# for DATA_COUNT in 240 2400 24000 240000
for FIELD_COUNT in 1 10 100
do
    for DATA_COUNT in 24 240 2400
    do
        figlet "${DATA_COUNT} - ${FIELD_COUNT}"
        for TEST_FILE in ./test-*.py
        do
            python prepare-test.py
            echo "BENCHMARK ${TEST_FILE} WITH ${DATA_COUNT} AND ${FIELD_COUNT} FIELDS"
            time python ${TEST_FILE} ${FIELD_COUNT} ${DATA_COUNT}
            echo ""
        done
    done
done