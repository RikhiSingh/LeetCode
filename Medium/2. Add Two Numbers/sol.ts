//  Link: https://leetcode.com/problems/add-two-numbers/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    // Initialize dummy head and current node
    const dummyHead: ListNode = new ListNode(0);
    let current: ListNode | null = dummyHead;
    let carry: number = 0;

    // Iterate through both lists until both are null and carry is 0
    while (l1 !== null || l2 !== null || carry !== 0) {
        // Calculate sum of current digits and carry
        const sum: number = (l1?.val ?? 0) + (l2?.val ?? 0) + carry;
        carry = Math.floor(sum / 10); // Calculate carry
        const digit: number = sum % 10; // Calculate digit

        // Create new node with digit and append it to the result list
        current.next = new ListNode(digit);
        current = current.next;

        // Move to next nodes in both lists
        l1 = l1?.next ?? null;
        l2 = l2?.next ?? null;
    }

    return dummyHead.next; // Return the result list, skipping the dummy head
};