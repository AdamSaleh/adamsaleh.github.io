.. title: Recreational Ocaml
.. slug: recreational-ocaml
.. date: 2019-10-11 14:17:37 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Some time ago, I decided to learn Ocaml on a whim. No project in mind, no use-case at work, just that weird 'huh, this sounds like an interesting language'.

I have dabbled in Haskell in college during few weeks (but the course was mostly focused on lazyness, recursion and anonymous functions, we didn't even touch 
I/O), I have used Clojure at work for a year or so, and both of these ventures into functional programming I liked, so trying out another FP languagee sounded like a pleasant exercise.

From what I heard, the type system didn't have type-classes I was used to from Haskell, but I decided I won't hold it against the language (and maybe try to grok the module-system later-on) and started searching for some sort of tutorial.

Here I came across the first thing that was a bit off, there seems to be several competing standard libraries. These days I am really used to languages having *batteries included* and having tothink about 'which flavour of map/fold/filter do I want to use?' seemed weird. In the end, I wen't with ecosystem from Jane Street, because their workshop looked really good.

Jane Street is a fin-tech firm that is probably the largest commercial user of Ocaml. They publish a lot of opensource libraries, including a core library (with all those List functioons you'd expect) and various helpers (i.e. support for asynchronous programming syntactic sugar through the ocaml ppx system, that seems like more restrained macro system you might see elsewhere)

But the workshop was really stellar.  There is a nice readme, several folder containing chapters, first chapter dedicated just to the installation of ocaml, including all the necessary libraries, complete with hello-world application and a simple test-case. 

Second chapter was dedicated to around twenty simple exercises guiding you through the basics of language and the chosen core library. This includes more in-dpth explanation of different ways to write test-cases, basics of recursion, pattern matching, list and string manipulation and even creation of your own data-structures.

What I really liked was how didactic most of these little exercises seemed. For example after you'd implement functions where one produces sum and other product of numbers in a list, shortly there'd be an exercise that points out how simmilar those two are, and you'd implement a generic version, and next exercise tells you 'you have just written List.fold function, so feel free to use it from now on'

After completing all of the smaller excercises, the next two chapters are 
If I  ever try to create a course, or a small workshop on language or library or tool, I am definitely stealing the format. 
