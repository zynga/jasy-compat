#!/usr/bin/env jasy

optimization = Optimization("blocks", "declarations", "variables", "privates")
formatting = Formatting()

session = Session()

@task("Writing Main")
def main():
    resolver = Resolver(session.getProjects())
    resolver.addClassName("compatty.Main")
    classes = Sorter(resolver).getSortedClasses()
    storeCompressed("main.js", classes, formatting=formatting, optimization=optimization)
    