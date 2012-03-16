#!/usr/bin/env jasy

@task("Build")
def build(dest="build"):
    resolver = Resolver().addClassName("compatty.Main")
    
    asset = Asset(resolver.getIncludedClasses())
    kernelClasses = storeKernel("%s/script/kernel.js" % dest, debug=True, assets=asset.exportBuild(buildFolder=dest))
    
    resolver.excludeClasses(kernelClasses)
    classes = Sorter(resolver).getSortedClasses()
    
    storeCompressed("%s/script/main.js" % dest, classes)
    copyFile("source/index.html", "build/index.html")
    
    
@task("Source")
def source():
    resolver = Resolver().addClassName("compatty.Main")

    asset = Asset(resolver.getIncludedClasses())
    kernelClasses = storeKernel("source/script/kernel.js", debug=True, assets=asset.exportSource())

    resolver.excludeClasses(kernelClasses)
    classes = Sorter(resolver).getSortedClasses()

    storeSourceLoader("source/script/main.js", classes)
