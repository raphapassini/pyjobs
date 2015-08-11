amplify.request.define( "jobs", "ajax", {
    url: "/api/jobs",
    dataType: "json",
    type: "GET"
});

/**
Act as list of job offers
**/
JobStore = function() {
    var _data =  []

    var getState = function(options) {
        var options = $.extend({
            force_reload: false
        }, options)

        if( !_data.length || options.force_reload ) {
            amplify.request("jobs", function(data) {
                _data = data
                amplify.publish('JobStore.change', data)
            })
        }
        return _data
    }

    return {
        getState: getState
    }
}()