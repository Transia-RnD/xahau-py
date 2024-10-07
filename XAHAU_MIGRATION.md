# xahau SDK Changes Overview

This document provides an overview of the key changes made in the xahau SDK, a fork of the original xrpl-py repository. Users transitioning from xrpl-py to xahau should take note of the following modifications to ensure a smooth migration and continued functionality.

## Key Changes

### 1. Import Statements
- The import statement for the SDK has changed:
  ```python
  import xrpl
  ```
  to:
  ```python
  import xahau
  ```

### 2. Client Class Import
- The import for the Client class has been updated:
  ```python
  from xrpl import Client
  ```
  to:
  ```python
  from xahau import Client
  ```

### 3. Exception Handling
- The exception class has been renamed:
  - From `XRPLException` to `XAHLException`.
  
  Update your exception handling code accordingly:
  ```python
  from xrpl.exceptions import XRPLException
  ```
  should now be:
  ```python
  from xahau.exceptions import XAHLException
  ```

### 4. Currency Class
- The currency class reference has changed:
  - From `XRP()` to `XAH()`.
  
  Ensure that any instances of `XRP()` are replaced with `XAH()` in your code.

### 5. Utility Functions
- The utility functions for converting between currency and drops have been renamed:
  - `xrp_to_drops()` is now `xah_to_drops()`
  - `drops_to_xrp()` is now `drops_to_xah()`
  
  Update your function calls accordingly:
  ```python
  drops = xrp_to_drops(amount)
  ```
  should now be:
  ```python
  drops = xah_to_drops(amount)
  ```

### 6. Ledger Calls
- Any calls to the XRPL ledger should continue to work seamlessly within this SDK. The underlying functionality remains intact, ensuring that users can interact with the XRPL ledger as expected.

## Conclusion

These changes are designed to enhance the xahau SDK while maintaining compatibility with the XRPL ledger. Users should review their code for the above modifications to ensure a smooth transition from xrpl-py to xahau. If you have any questions or need further assistance, please refer to the documentation or reach out to the community for support.