#!/usr/bin/env jasy

@task("Clean")
def clean():
    session.clearCache()

@task("Build")
def build():
    setPrefix("build")
    
    resolver = Resolver().addClassName("compatty.Main")
    
    asset = Asset(resolver.getIncludedClasses())
    kernelClasses = storeKernel("script/kernel.js", debug=True, assets=asset.exportBuild())
    
    resolver.excludeClasses(kernelClasses)
    classes = Sorter(resolver).getSortedClasses()
    
    storeCompressed("script/main.js", classes)
    copyFile("source/index.html", "index.html")
    
    
@task("Source")
def source():
    setPrefix("source")
    
    resolver = Resolver().addClassName("compatty.Main")

    asset = Asset(resolver.getIncludedClasses())
    kernelClasses = storeKernel("script/kernel.js", debug=True, assets=asset.exportSource())

    resolver.excludeClasses(kernelClasses)
    classes = Sorter(resolver).getSortedClasses()

    storeSourceLoader("script/main.js", classes)
