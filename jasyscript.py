#!/usr/bin/env jasy

session = Session()
optimization = Optimization("blocks", "declarations", "variables", "privates")
formatting = Formatting()

@task("Build")
def build():
    buildFolder = "build"
    
    resolver = Resolver(session.getProjects())
    resolver.addClassName("compatty.Main")
    
    asset = Asset(session, resolver.getIncludedClasses())
    kernelClasses = storeKernel("%s/script/kernel.js" % buildFolder, session, debug=True, assets=asset.exportBuild(buildFolder=buildFolder))
    
    resolver.excludeClasses(kernelClasses)
    classes = Sorter(resolver).getSortedClasses()
    
    storeCompressed("%s/script/main.js" % buildFolder, classes, formatting=formatting, optimization=optimization)
    copyFile("source/index.html", "build/index.html")
    
    
@task("Source")
def source():
    resolver = Resolver(session.getProjects())
    resolver.addClassName("compatty.Main")

    asset = Asset(session, resolver.getIncludedClasses())
    kernelClasses = storeKernel("source/script/kernel.js", session, debug=True, assets=asset.exportSource())

    resolver.excludeClasses(kernelClasses)
    classes = Sorter(resolver).getSortedClasses()

    storeSourceLoader("source/script/main.js", classes, session)
