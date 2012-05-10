betterast
=========

An AST for python. I have about 10 versions of this class floating around my
code tree. I decided to make a "cannonical" version. Since cannon means "list" 
and cannonical means "on the list," by cannonical I mean on my list of public
projects. The code for this AST is short but flexible.

What's in the box
-----------------

An AST `Node` which has a `label` and `children`. That's it! Simple but useful.

### Features of the AST Node

- Pre-order traversal (via `__iter__`)
- Declaritive construction (via the `.addkid()` method)
- Serialization (via `__str__`) in pre-order.
- De-Serialization (via the `build_tree` method). This isn't in the `Node` class
  itself but included in the package.
- Graphviz based visualization (via the `dotty` method).

Other versions of this particular AST have included automatic tree (equality)
comparison. I will consider adding this back. As a further note, this AST
package is compatible with my (Zhang-Shasha Tree Edit
Distance)[https://github.com/timtadh/zhang-shasha] package.


