#!/usr/bin/env bash
TESTS=$(grep -l main micro-benchmarks/*.c micro-benchmarks/*.cpp)
LYFLAG="micro-benchmarks/utilities/polybench.c -I micro-benchmarks -I micro-benchmarks/utilities -DPOLYBENCH_NO_FLUSH_CACHE -DPOLYBENCH_TIME -D_POSIX_C_SOURCE=200112L"

 
for test in $TESTS; do
            echo "------------------------------------------"
            echo "RUNNING: $test"
            CFLAGES="" 
            if grep -q 'PolyBench' "$test"; then CFLAGS+=" $POLYFLAG"; fi
            clang -Xclang $CFLAGS -load -Xclang $HOME/OpenMP-Extractor/lib/ompextractor/libCLANGOMPExtractor.so -Xclang -add-plugin -Xclang -extract-omp -fopenmp -g -O0 -c -fsyntax-only "$test"
        done


JTESTS=$(grep -l main micro-benchmarks/*.json)

for test in $JTESTS; do
	        echo "------------------------------------------"
            echo "RUNNING: $test" >> pra.txt
            python3 extractorparser.py "$test" >> pra.txt
        done
