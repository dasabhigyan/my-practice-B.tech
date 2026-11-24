# Read three integer quiz scores, one per line.
# If the average of the three scores is strictly greater than 80 
# AND every individual score is at least 60, print "Distinction awarded."
# Otherwise, print "No distinction awarded."
score1 = int(input())
score2 = int(input()) 
score3 = int(input())
avg = (score1 + score2 + score3)/3
if avg > 80:
        if score1 > 60 and score2 > 60 and score3 > 60:
                print("Distinction awarded.")
        else:
                print("No distinction awarded.")
else:
        print("No distinction awarded.")
