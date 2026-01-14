# File Location Information

## LICENSE File Location

The LICENSE file has been moved to `.github/LICENSE`.

**GitHub Detection**: ✅ GitHub will still detect and display the license information correctly when it's located in the `.github/` directory. GitHub looks for LICENSE files in multiple locations:
- Root directory
- `.github/` directory  
- `docs/` directory

## README.md File Location

The README.md file **remains in the root directory**.

**Important**: README.md must stay in the root directory to be displayed on the repository's main page. GitHub only displays README.md files that are located in the root of the repository. If moved to `.github/`, it would not appear on the main repository page.

## Summary

- ✅ **LICENSE**: Can be in `.github/` - still detected by GitHub
- ❌ **README.md**: Must stay in root - won't show on main page if moved to `.github/`
