// Tabs
function init_Tabs() {
    // put all tabs captions into holder
    $( ".tabs li" ).appendTo( $( ".nav-tabs" ) );
    // put all tabs contents into holder
    $( ".tab-pane" ).appendTo( $( ".tab-content" ) );
    // make first tab active
    $( ".tabs li:first-child" ).addClass( "active" );
    $( ".tab-pane:first-child" ).addClass( "active" );

    // add hrefs to tabs captions for tabs toggling
    var i = 0;
    $( ".tabs li a" ).each(function() {
        i++;
        $( this ).attr('href', '#' + i);
    });

    // add ids to tabs contents for tabs toggling
    var n = 0;
    $( ".tab-pane" ).each(function() {
        n++;
        $( this ).attr('id', n);
    });
}