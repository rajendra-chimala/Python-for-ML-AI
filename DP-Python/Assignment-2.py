# This is assignment 2 for the Data Processing course.
import time

def main():
    DIRT = [True, True]
    VACUUM = [True, False]  
    my_ai_agent(DIRT, VACUUM)

def my_ai_agent(D, V):
    while D[0]==True or D[1]==True:
        if V[0]==True:
            print("[ VACUUM CLEANER IS IN ROOM A ]")
            time.sleep(3)
            if D[0] and D[1]:
                print("ROOM [A] : [🧹______.__.__.._____..____...____...__________...___._____._____._]")
                print("ROOM [B] : [__.._.___.__.__.._____..____...____...__________...___._____._____._]")
            elif D[0]==True and D[1]==False:
                print("ROOM [A] : [🧹______.__.__.._____..____...____...__________...___._____._____._]")
                print("ROOM [B] : [____________________________________________________________________]")
            elif D[0]==False and D[1]==True:
                print("ROOM [A] : [🧹_________________________________________________________________]")
                print("ROOM [B] : [__.._.___.__.__.._____..____...____...__________...___._____._____._]")

            if D[0]==True:
                print("[DIRT FOUND IN ROOM A ]")
                time.sleep(3)
                print("[DIRT CLEANING.......]")
                time.sleep(2)
                print("[ROOM A CLEAR SUCCESSFULLY !]")
                time.sleep(3)
                D[0] = False
                if D[1]==True:
                    print("ROOM [A] : [_________________________________________________________________🧹]")
                    print("ROOM [B] : [__.._.___.__.__.._____..____...____...__________...___._____._____._]")
                else:
                    print("ROOM [A] : [_________________________________________________________________🧹]")
                    print("ROOM [B] : [____________________________________________________________________]")
                print("[MOVING TO ROOM B]")
                time.sleep(2)
                V[0] = False
                V[1] = True
            else:
                print("[NO DIRT FOUND IN ROOM A]")
                time.sleep(3)
                print("[MOVING TO ROOM B]")
                time.sleep(3)
                V[0] = False
                V[1] = True

        elif V[1]==True:
            print("[ VACUUM CLEANER IS IN ROOM B ]")
            time.sleep(1)
            if D[0]==True and D[1]==True:
                print("ROOM [A] : [____________________________________________________________________]")
                print("ROOM [B] : [🧹.._.___.__.__.._____..____...____...__________...___._____._____._]")
            elif D[0]==True and D[1]==False:
                print("ROOM [A] : [____________________________________________________________________]")
                print("ROOM [B] : [🧹__________________________________________________________________]")
            elif D[0]==False and D[1]==True:
                print("ROOM [A] : [____________________________________________________________________]")
                print("ROOM [B] : [🧹.._.___.__.__.._____..____...____...__________...___._____._____._]")

            if D[1]==True:
                print("[DIRT FOUND IN ROOM B ]")
                time.sleep(3)
                print("[DIRT CLEANING.......]")
                time.sleep(3)
                print("[ROOM B CLEAR SUCCESSFULLY !]")
                time.sleep(2)
                D[1] = False
                print("ROOM [A] : [____________________________________________________________________]")
                print("ROOM [B] : [_________________________________________________________________🧹]")
                print("[MOVING TO ROOM A]")
                
                time.sleep(2)
                V[1] = False
                V[0] = True
            else:
                print("[NO DIRT FOUND IN ROOM B]")
                time.sleep(3)
                print("[MOVING TO ROOM A]")
                
                time.sleep(2)
                V[1] = False
                V[0] = True

    print("[ALL ROOMS ARE CLEANED SUCCESSFULLY !]")
    print("ROOM [A] : [🧹______________________________________________________________]")
    print("ROOM [B] : [_________________________________________________________________]")

main()
