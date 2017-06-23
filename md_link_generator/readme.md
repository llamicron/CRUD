# Markdown Link Generator
This crystal program will find all the `.md` files in your project, and generate a link to each of them.

# Installation
First, clone the repo:
```
$ git clone http://github.com/llamicron/md_link_generator.git
```

If you don't have Crystal Lang installed, just move the `md_link_gen` file into somewhere in your `$PATH`, like `/usr/local/bin`.

If you do have crystal installed, you can run `crystal build md_link_gen.cr` to build the latest version, then follow the step above to move it into your path. _Note_: I will try to build a new binary every time I push to github, so running `crystal build` will usually have no effect.

# Usage
From your projects root, run:
```
md_link_gen
```
Or, slap that output to the end of your `readme.md` like so:
```
md_link_gen >> readme.md
```

I ran `md_link_gen >> readme.me` and this is what is put into `readme.md`:

[md/md_sub1/md_sub_sub1/test2](md/md_sub1/md_sub_sub1/test2.md)

[md/md_sub1/md_sub_sub2/test3](md/md_sub1/md_sub_sub2/test3.md)

[md/md_sub1/test2](md/md_sub1/test2.md)

[md/md_sub2/test2](md/md_sub2/test2.md)

[md/test2](md/test2.md)

[md/test3](md/test3.md)

[md2/test4](md2/test4.md)

[md2/test5](md2/test5.md)

[readme](readme.md)

As you can see, it's just a long list of links. This is meant to generate links for a large number of files, and then you can copy and paste them where you need them. This is useful for programs with self-written docs or instructions written in markdown.

If you don't direct it into a file, the links will be displayed in your terminal. Just copy and paste them wherever you want.
