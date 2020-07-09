/*
!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!
!!! Copyright (c) 2017-20, Lawrence Livermore National Security, LLC
!!! and DataRaceBench project contributors. See the DataRaceBench/COPYRIGHT file for details.
!!!
!!! SPDX-License-Identifier: (BSD-3-Clause)
!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!
*/

/*
No data race. The data environment of the task is created according to the
data-sharing attribute clauses, here at line:27 it is var. Hence, var is
modified 10 times, resulting to the value 10.
*/

#include <omp.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
  int var = 0;
  int i;

  #pragma omp parallel for shared(var) schedule(static,1)
  for (i = 0; i < 10; i++) {
    #pragma omp task shared(var) if(1)
    {
      var++;
    }
  }

  int error = (var != 10);
  fprintf(stderr, "DONE %d \n",var);
  return error;
}
