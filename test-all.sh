for DATA_COUNT in 240 2400 24000 240000 2400000
do
    figlet ${DATA_COUNT}
    for TEST_FILE in ./test-*.py
    do
        echo "BENCHMARK ${TEST_FILE} WITH ${DATA_COUNT} data"
        time python ${TEST_FILE} ${DATA_COUNT}
        echo ""
    done
done