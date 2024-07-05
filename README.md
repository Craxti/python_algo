# Algorithms Repository

This repository contains implementations of various algorithms, including consensus algorithms, digital signatures, hashing, sorting algorithms, and more. Each algorithm is implemented in its respective Python file, and examples and complexity analyses are provided.

## Directory Structure

- `blockchain_algo/`
  - `Consensus_Algorithms.py`: Implementation of various consensus algorithms.
  - `Digital_Signatures.py`: Implementation of digital signature algorithms.
  - `Hashing.py`: Implementation of hashing algorithms.
  - `Merkle_Tree.py`: Implementation of Merkle tree data structure.
  - `PoS.py`: Implementation of Proof of Stake algorithm.
  - `PoW.py`: Implementation of Proof of Work algorithm.

- `coding_algo/`
  - `Burrows_Wheeler_Transform.py`: Implementation of Burrows-Wheeler Transform algorithm.
  - `DEFLATE.py`: Implementation of DEFLATE compression algorithm.
  - `Huffman_Coding.py`: Implementation of Huffman Coding algorithm.
  - `Lempel_Ziv_Welch.py`: Implementation of Lempel-Ziv-Welch (LZW) algorithm.
  - `LZ77_LZ78.py`: Implementation of LZ77 and LZ78 compression algorithms.
  - `Run_Length_Encoding.py`: Implementation of Run-Length Encoding algorithm.

- `sorted_algo/`
  - `B_Tree_Sort.py`: Implementation of B-Tree Sort algorithm. [README_B_Tree.md](sorted_algo/B_Tree_Sort/README_B_Tree.md)
  - `Bitonic_Sort.py`: Implementation of Bitonic Sort algorithm. [README_Bitonic.md](sorted_algo/Bitonic_Sort/README_Bitonic.md)
  - `Block_Sort.py`: Implementation of Block Sort algorithm. [README_Block.md](sorted_algo/Block_Sort/README_Block.md)
  - `Bubble_Sort.py`: Implementation of Bubble Sort algorithm. [README_bubble.md](sorted_algo/Bubble_Sort/README_bubble.md)
  - `Bucket_Sort.py`: Implementation of Bucket Sort algorithm. [README_Bucket.md](sorted_algo/Bucket_Sort/README_Bucket.md)
  - `Cocktail_Shaker_Sort.py`: Implementation of Cocktail Shaker Sort algorithm. [README_Cocktail_Shaker.md](sorted_algo/Cocktail_Shaker_Sort/README_Cocktail_Shaker.md)
  - `Counting_Sort.py`: Implementation of Counting Sort algorithm. [README_Counting.md](sorted_algo/Counting_Sort/README_Counting.md)
  - `Gnome_Sort.py`: Implementation of Gnome Sort algorithm. [README_Tournament_Gnome.md](sorted_algo/Gnome_Sort/README_Tournament_Gnome.md)
  - `Heap_Sort.py`: Implementation of Heap Sort algorithm. [README_Heap.md](sorted_algo/Heap_Sort/README_Heap.md)
  - `Insertion_Sort.py`: Implementation of Insertion Sort algorithm. [README_Insertion.md](sorted_algo/Insertion_Sort/README_Insertion.md)
  - `Interpolation_Sort.py`: Implementation of Interpolation Sort algorithm. [README_Interpolation.md](sorted_algo/Interpolation_Sort/README_Interpolation.md)
  - `Merge_Sort.py`: Implementation of Merge Sort algorithm. [README_Merge.md](sorted_algo/Merge_Sort/README_Merge.md)
  - `Pyramid_Sort.py`: Implementation of Pyramid Sort algorithm. [README_Pyramid.md](sorted_algo/Pyramid_Sort/README_Pyramid.md)
  - `Quick_Sort.py`: Implementation of Quick Sort algorithm. [README_Quick.md](sorted_algo/Quick_Sort/README_Quick.md)
  - `Radix_Sort.py`: Implementation of Radix Sort algorithm. [README_Radix.md](sorted_algo/Radix_Sort/README_Radix.md)
  - `Selection_Sort.py`: Implementation of Selection Sort algorithm. [README_Selection.md](sorted_algo/Selection_Sort/README_Selection.md)
  - `Shell_Sort.py`: Implementation of Shell Sort algorithm. [README_Shell.md](sorted_algo/Shell_Sort/README_Shell.md)
  - `Smoothsort.py`: Implementation of Smoothsort algorithm. [README_Smoothsort.md](sorted_algo/Smoothsort/README_Smoothsort.md)
  - `Timsort.py`: Implementation of Timsort algorithm. [README_Timsort.md](sorted_algo//README_Timsort.md)
  - `Tournament_Sort.py`: Implementation of Tournament Sort algorithm. [README_Tournament.md](sorted_algo/Tournament_SortTimsort/README_Tournament.md)
  - `Tree_Sort.py`: Implementation of Tree Sort algorithm. [README_Tree.md](sorted_algo/Tree_Sort/README_Tree.md)
  - `Weave_Sort.py`: Implementation of Weave Sort algorithm. [README_Weave.md](sorted_algo/Weave_Sort/README_Weave.md)

## Algorithm Descriptions and Complexity

### Blockchain Algorithms
- **Consensus Algorithms**: Implementations of various consensus mechanisms like Proof of Work (PoW) and Proof of Stake (PoS). These algorithms are fundamental to blockchain technology, ensuring agreement on the blockchain state.
- **Digital Signatures**: Implementation of cryptographic digital signatures for secure communication.
- **Hashing**: Various hashing algorithms to secure and verify data integrity.
- **Merkle Tree**: Implementation of Merkle Tree, used for efficient and secure verification of data in blockchain.
- **Proof of Stake (PoS)**: An energy-efficient consensus algorithm that selects validators based on their stake in the network.
- **Proof of Work (PoW)**: A consensus algorithm that requires miners to solve cryptographic puzzles to add new blocks to the blockchain.

### Coding Algorithms
- **Burrows-Wheeler Transform (BWT)**: A data transformation algorithm used in data compression.
  - **Complexity**: Time: O(n), Space: O(n)
- **DEFLATE**: A compression algorithm that combines the LZ77 algorithm and Huffman coding.
  - **Complexity**: Varies depending on implementation and data.
- **Huffman Coding**: A lossless data compression algorithm.
  - **Complexity**: Time: O(n log n), Space: O(n)
- **Lempel-Ziv-Welch (LZW)**: A universal lossless data compression algorithm.
  - **Complexity**: Time: O(n), Space: O(n)
- **LZ77 and LZ78**: Data compression algorithms that form the basis for many other compression algorithms.
  - **Complexity**: Time: O(n), Space: O(n)
- **Run-Length Encoding (RLE)**: A simple form of data compression where runs of data are stored as a single data value and count.
  - **Complexity**: Time: O(n), Space: O(n)

### Sorting Algorithms
- **B-Tree Sort**: Sorts data using a B-tree structure.
  - **Complexity**: Time: O(n log n), Space: O(n)
- **Bitonic Sort**: A parallel algorithm for sorting.
  - **Complexity**: Time: O(log^2 n), Space: O(n log n)
- **Block Sort**: Similar to merge sort but divides array into blocks.
  - **Complexity**: Time: O(n log n), Space: O(n)
- **Bubble Sort**: A simple comparison-based sorting algorithm.
  - **Complexity**: Time: O(n^2), Space: O(1)
- **Bucket Sort**: Distributes elements into buckets and then sorts each bucket.
  - **Complexity**: Time: O(n + k), Space: O(n + k)
- **Cocktail Shaker Sort**: A variation of bubble sort that sorts in both directions.
  - **Complexity**: Time: O(n^2), Space: O(1)
- **Counting Sort**: Non-comparison-based sorting algorithm.
  - **Complexity**: Time: O(n + k), Space: O(k)
- **Gnome Sort**: Similar to insertion sort but swaps elements to their correct position.
  - **Complexity**: Time: O(n^2), Space: O(1)
- **Heap Sort**: A comparison-based sorting algorithm using a heap.
  - **Complexity**: Time: O(n log n), Space: O(1)
- **Insertion Sort**: Builds sorted array one element at a time.
  - **Complexity**: Time: O(n^2), Space: O(1)
- **Interpolation Sort**: A variant of binary search.
  - **Complexity**: Time: O(n log n), Space: O(1)
- **Merge Sort**: A divide and conquer algorithm.
  - **Complexity**: Time: O(n log n), Space: O(n)
- **Pyramid Sort**: Similar to heap sort.
  - **Complexity**: Time: O(n log n), Space: O(n)
- **Quick Sort**: A divide and conquer algorithm.
  - **Complexity**: Average: O(n log n), Worst: O(n^2), Space: O(log n)
- **Radix Sort**: Non-comparison-based sorting algorithm.
  - **Complexity**: Time: O(nk), Space: O(n + k)
- **Selection Sort**: Simple comparison-based sorting algorithm.
  - **Complexity**: Time: O(n^2), Space: O(1)
- **Shell Sort**: Generalization of insertion sort.
  - **Complexity**: Time: O(n log n), Space: O(1)
- **Smoothsort**: A variation of heapsort.
  - **Complexity**: Best: O(n), Average/Worst: O(n log n), Space: O(1)
- **Timsort**: Hybrid sorting algorithm derived from merge sort and insertion sort.
  - **Complexity**: Time: O(n log n), Space: O(n)
- **Tournament Sort**: A sorting algorithm based on tournament tree.
  - **Complexity**: Time: O(n log n), Space: O(n)
- **Tree Sort**: Sorts elements by inserting them into a binary search tree.
  - **Complexity**: Time: O(n log n), Space: O(n)
- **Weave Sort**: An advanced sorting algorithm (details needed).
  - **Complexity**: Varies

## Running the Algorithms

Each algorithm can be run independently. Example usages and test cases are provided within each script. To run an algorithm, execute the corresponding Python file. For example:

```bash
python sorted_algo/Quick_Sort.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements or additions.


## License
This repository is licensed under the MIT License.


This `README.md` file provides an overview of your repository's structure, describes each algorithm and its complexity, and gives instructions on how to run the algorithms. Adjustments may be needed based on the specific details of each implementation and any additional documentation you have.