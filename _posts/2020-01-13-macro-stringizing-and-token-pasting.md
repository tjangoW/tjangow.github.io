---
tags: c++, macro
---

So basically, macros is a way of automating typing of code 
(or at least for most of my use cases). 
Just found out about two operators which are quite useful for this, which are the
- `#` stringizing operator and
- `##` token-pasting operator

Guess their names are pretty indicative of their functions?

In any case, **stringizing operator** obviously stringify whatever input to string, which can be useful 
for e.g. 
```cpp
#define DEBUG(var) { cout << #var " = " << var; }
```

**Token-pasting**, on the other hand, joins *tokens* together. 
Tokens, in short, are the smallest unit that is meaningful for the compiler.
What token-pasting operator does is joining two or more tokens together so as to be interpreted together.
Example:
```cpp
std::shared_ptr<ui_object> var_very_long_name_menu, var_very_long_name_GUI, var_very_long_name_interface;
#define LOG(comp) { auto& ref = var_very_long_name_ ## comp; \
                    cout << ref.title << "\n" << and_so_on(ref); }
LOG(menu)
```

## Sources
- [microsoft VS 2019 docs](https://docs.microsoft.com/en-us/cpp/preprocessor/preprocessor-operators?view=vs-2019)
