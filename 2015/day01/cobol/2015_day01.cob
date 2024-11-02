      $set sourceformat(free)
       IDENTIFICATION DIVISION.
       PROGRAM-ID. AoC_2015_day01.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT INPUT-FILE
           ASSIGN TO "../input.txt"
           ORGANIZATION IS SEQUENTIAL
           FILE STATUS IS FILE-STATUS.
       
       DATA DIVISION.
       FILE SECTION.
       FD  INPUT-FILE.
       01  INPUT-CHAR  PIC X.
       
       WORKING-STORAGE SECTION.
       01 FILE-STATUS PIC X(2).
           88 FILE-OK  VALUE "00".
           88 FILE-EOF VALUE "10".
       01 END-OF-FILE-FLAG     PIC X VALUE "N".
           88 END-OF-FILE VALUE "Y".
       01 FLOOR PIC S9(8) VALUE 0.
       
       PROCEDURE DIVISION.
       MAIN-PARA.
           PERFORM OPEN-FILE
           PERFORM READ-STEPS UNTIL END-OF-FILE
           DISPLAY "Santa ends on floor: " FLOOR
           PERFORM CLOSE-FILE
           STOP RUN.
       
       OPEN-FILE.
           OPEN INPUT INPUT-FILE
           IF NOT FILE-OK
               DISPLAY "Error opening file. Status: " FILE-STATUS
               STOP RUN
           END-IF.
       
       READ-STEPS.
           READ INPUT-FILE
               AT END
                   SET END-OF-FILE TO TRUE
               NOT AT END
                   PERFORM PROCESS-STEP
           END-READ.
       
       PROCESS-STEP.
           EVALUATE INPUT-CHAR
               WHEN "("
                   PERFORM FLOOR-UP
               WHEN ")"
                   PERFORM FLOOR-DOWN
           END-EVALUATE.

       FLOOR-UP.
           ADD 1 TO FLOOR.
           
       FLOOR-DOWN.
           SUBTRACT 1 FROM FLOOR.
       
       CLOSE-FILE.
           CLOSE INPUT-FILE.
