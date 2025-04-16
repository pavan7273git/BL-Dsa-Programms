from binarysearchtree import Binarysearchtree



def main():
    bst = Binarysearchtree()
    bst.root = bst.insert(bst.root , 50)
    bst.root = bst.insert(bst.root , 30)
    bst.root = bst.insert(bst.root , 20)
    bst.root = bst.insert(bst.root , 40)
    bst.root = bst.insert(bst.root , 70)
    bst.root = bst.insert(bst.root , 60)
    bst.root = bst.insert(bst.root , 80)
    bst.inOrderTraversal(bst.root)
    print()

    found = bool(bst.search(bst.root , 40))
    print(found)

    bst.root = bst.update(bst.root , 40, 45)
    bst.inOrderTraversal(bst.root)
    print()

    bst.root = bst.delete(bst.root , 45)
    bst.inOrderTraversal(bst.root)

if __name__ == "__main__":
    main()
