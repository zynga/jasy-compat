/**
 * Test for playing with 3rd party code
 */
(function() {

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
