"""
Exercise 4: Nightclub VIP Queue
Scenario: A nightclub bouncer maintains a list of VIP guests who are allowed inside: ["Guido", "Esha", "Rajan", "Kishori"].
 As guests arrive at the door, the bouncer prompts the user to enter their name.

If the guest is on the VIP list, move them from their current position in the queue and insert them at the front of the queue (index 0).
If the guest is not on the VIP list, print "Access denied. Not on the VIP list." 
and do not modify the list. Run this program in a loop. The loop should stop when the user types "exit".
Print the updated queue state after each guest arrives.

Sample Walkthrough:
Current VIP queue: ['Guido', 'Esha', 'Rajan', 'Kishori']
Enter guest name: Rajan
Rajan moved to the front!
Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

Enter guest name: Vinod
Access denied. Not on the VIP list.
Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

Enter guest name: exit
"""
def main():
    vip_queue = ["Guido", "Esha", "Rajan", "Kishori"]
    while True:
        n = input("Enter guest name: ").title()
        if n == "Exit":
            return
        if n in vip_queue:
            vip_queue.remove(n)
            vip_queue.insert(0, n)
            print(f"Current VIP queue: {vip_queue}")
        else:
            print("Access denied. Not on the VIP list.")
        

print("="*110)
main()