# Static Site Generator

## Overview

This Static Site Generator project converts MD files to HTML files by recursively copying directories and files from a source directory to an output directory. This projects eliminates the need to create from scratch static webpages that follow a single stylesheet (you may need to write this stylesheet). Simply bring the Markdown files, the assets and images, and have this program output the needed HTML files.

The technologies used to build this program are the following:

- Language: Python
- Tools: Shell scripting
- Text Editor: Neovim

The learning goals of this project are the following:

1. **Static Sites**: Learn about what a static site is, and start building the functionality necessary to process and move static HTML and Markdown files.
2. **Nodes**: Build the core HTML generation logic that will power the Static Site Generator. Use recursion and OOP principles to build and easily understandable and maintainable system.
3. **Inline**: Build the inline markdown parsing logic, and the logic to generate inline HTML elements.
4. **Block**: Handle entire blocks of markdown, and generate the HTML nodes that represent them.
5. **Website**: Put the entire Static Site Generator together and publish website.

## How to Use

1. Fork this repo so that you can have your own copy that you can modify, then install by forking to your machine.

> Your fork's URL will be something like this: `https://github.com/<your_github_username>/static-site-generator`

2. Place all markdown files and directories and in `content/`
3. Place all static assets like images and CSS in `static/`
4. Run the build shell script by running the command `./build.sh` from the root of the project
5. Ensure all markdown files have now been copied over to the `docs/` directory
6. Push code to your own repo


## Challenges and Growth

This program was a guided learning project from [Boot.dev](https://www.boot.dev/courses/build-static-site-generator-python) with many challenges to practice techniques that follow Object Oriented Programming Principles and Functional Programming Principles.

1. **Static Site Generation**: With experience in Frontend Development and familiarity with HTML, CSS, and JavaScript, I had previously (maybe naively) believed that many websites were built from scratch and that the HTML, CSS, and JavaScript were written from scratch. This project helped me realise that on one hand: there exists tools that help developers increase their speed in producing software, but on the other hand, these tools are only as helpful as their limits. For sites where the majority of content is static (unmoving) this tool is perfect, but for sites that are more _dynamic_ and require lots of user interaction, this tool is useless.

2. **Understanding the DOM through Python**: From Frontend Development its common knowledge to understand that the browser parses the HTML and builds the DOM one node at a time, which makes HTML a VERY declarative language. But to construct the Python logic to distinguish a block of Markdown text as the correct block HTML tag and the text within the block as the correct inline HTML tag was very challenging but very rewarding.

3. **Writing Unit Tests**: When parsing an entire markdown file or files which could be incredibly long with lots of text and information, there are plenty of pitfalls that can cause the code the break. This project opened my eyes to the security _but also frustration_ in writing lots of unit tests. Unit tests provide the reassurance that my code works in the _known_ edge cases, and although working through these edge cases can be challenging, they do provide security in knowing that my code has been tested to some extent.

4. **Real World Use Cases for Recursion**: Before this project, I had only known about recursion through problems to do with Data Structures and Algorithms, but using recursion as a method to traverse the file tree, to create ParentNodes with nested children, to convert an entire Markdown document into HTML was deeply satisfying.

5. **Using Enums for Types**: Before this project, I had little to no experience with Enums, but using Enums to create a fixed set of types allowed for controlled constraints when dealing with various blocks of text.

6. **Regex Pattern Matching**: Regex has always been a box of mystery for me with scary syntax and unreadable patterns, but this project forced me to look more deeply into regexes and learn the syntax to create more complex patterns to match with links and images in Markdown.


