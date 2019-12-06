const { test } = QUnit;

test( "square()", t => {
  t.equal( square( 2 ), 4, "square(2) equals 4" );
  t.equal( square( 3 ), 9, "square(3) equals 9" );
});