#!/usr/bin/env jasy

@task("Build")
def build():
    buildFolder = "build"
    
    resolver = Resolver()
    resolver.addClassName("compatty.Main")
    
    asset = Asset(resolver.getIncludedClasses())
    kernelClasses = storeKernel("%s/script/kernel.js" % buildFolder, debug=True, assets=asset.exportBuild(buildFolder=buildFolder))
    
    resolver.excludeClasses(kernelClasses)
    classes = Sorter(resolver).getSortedClasses()
    
    storeCompressed("%s/script/main.js" % buildFolder, classes)
    copyFile("source/index.html", "build/index.html")
    
    
@task("Source")
def source():
    resolver = Resolver()
    resolver.addClassName("compatty.Main")

    asset = Asset(resolver.getIncludedClasses())
    kernelClasses = storeKernel("source/script/kernel.js", debug=True, assets=asset.exportSource())

    resolver.excludeClasses(kernelClasses)
    classes = Sorter(resolver).getSortedClasses()

    storeSourceLoader("source/script/main.js", classes)
