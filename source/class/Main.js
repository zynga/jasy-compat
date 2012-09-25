/**
 * Test for playing with 3rd party code
 *
 * #asset(qunit-xyz.css)
 * #asset(jquery-ui.css)
 * #require(core.io.StyleSheet)
 */
(function() {

	// Asset loading feature tests
	// Use the name of the files you have defined in your jasyproject.conf
	core.io.Asset.load(["qunit-xyz.css"], function() {
		console.debug("QUnit style sheet loaded!");
	});

	core.io.Asset.load(["jquery-ui.css"], function() {
		console.debug("jQuery UI style sheet loaded!");
	});

	// Testing existance of classes/modules
	console.debug("Has jQuery Object:", !!$)
	console.debug("Has jQuery UI Object:", !!$.ui)
	console.debug("Has QUnit Object:", !!QUnit);
	console.debug("Has Slang Object:", !!slang);
	console.debug("Has Sizzle Object:", !!Sizzle);
	console.debug("Has NWEvents Object:", !!NW.Event);
	console.debug("Has Modernizr Object:", !!Modernizr);
	console.debug("Has $LAB Object:", !!$LAB);
	console.debug("Has XRegExp Object:", !!XRegExp);
	console.debug("Has Hogan Object:", !!Hogan && !!Hogan.compile);
	console.debug("Has History Object:", !!History);
	console.debug("Has Underscore Object:", !!_);
	
})();
