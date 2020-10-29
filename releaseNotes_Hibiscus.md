### version 3.0 Hibiscus

The latest version of Tea.lock has been nicknamed Hibiscus, after the herbal tea made from the red hibiscus flower.

Read below for details on several improvements and changes included with Hibiscus.

#### Longer keys
Keys are now 20 bits instead of 12. This increases Tea.lock's security, as a 20-bit key is much more difficult for an adversary to guess than a 12-bit key.

#### Redesigned teacup
Tea.lock's user interface, called the teacup, has been modified to be more user-friendly. Input/output cells are now adjacent to each other rather than on top of each other, and alerts about invalid keys have also been moved.

#### Debug has been moved to the teacup
To make debugging simpler, the debug table has been moved from the development sheet to the main sheet, the teacup. The debug cells remain empty until you enter 1 into cell A2.

#### Added layers of encryption
Before reaching Tea.lock's regular encryption processes, plaintext is now put through a system nicknamed "Spout." The additional two layers of encryption, spout 1 and spout 2, are stream cipers, meaning the plaintext is encrypted bit-wise rather than block-wise; each incremental bit is encrypted using the previously encrypted bit. The intention is to add more of an avalanche effect to the output. If you change your plaintext even slightly, Tea.lock's ciphertext output will often become significantly different.

#### Other backend improvements and fixes
Other minor but effective changes have been made. These include changes that make backwards compatibility impossible, so ciphertext produced with previous versions of Tea.lock will not be decipherable with Hibisicus.
