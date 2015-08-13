function do_redirect(url) {
    redirect_url = location.search.split('=')[1]
    location.href = decodeURIComponent( redirect_url )
}

$(document).ready(function() {
    if( location.search.indexOf('goto') == -1 )
        return false
    else
        do_redirect()
})