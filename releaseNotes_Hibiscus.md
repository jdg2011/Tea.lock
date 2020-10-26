### version 3.0 Hibiscus

The latest version of Tea.lock has been nicknamed Hibiscus, after the herbal tea made from red hibiscus flower.

Hibiscus includes several improvements and changes, including

#### Longer keys
Keys are now 20 bits instead of 12. This increases Tea.lock's security, as a 20-bit key is much more difficult to guess than a 12-bit key.

#### Redesigned teacup
Tea.lock's user interface, called the teacup, has been modified to be more user-friendly. Input/output cells are now adjacent to each other rather than on top of each other, and alerts about invalid keys have also been moved.

#### Debug has been moved to the teacup
To make debugging simpler, the debug table has been moved to the main sheet, the teacup. The debug cells remain empty until you enter 1 into cell A2.

#### Added layers of encryption
Before reaching Tea.lock's regular encryption processes, plaintext is now put through a system called "Spout." The additional two layers of encryption are stream cipers, meaning the plaintext is encrypted piece-wise rather than block-wise, and the key to decipering each encrypted piece is in the previous piece. The intention is to add more of an avalanche effect to the output. If you change your plaintext even slightly, the ciphertext that Tea.lock produces should be significantly different.

#### Other backend improvements and fixes
Other minor but effective changes have been made. These include changes that make backwards compatibility impossible, so ciphertext produced with previous versions of Tea.lock will not be decipherable with Hibisicus.  
