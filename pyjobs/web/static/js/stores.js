/**
Construct a new Store object of a given name and resource
**/
var BaseStore = function(storeName, resource_name) {
    var _data =  []
    var _filters = {}
    var _filter_change = false

    amplify.request.define( resource_name, "ajax", {
        url: "/api/" + resource_name,
        dataType: "json",
        type: "GET"
    });

    /** Get current object state **/
    function getState(force_reload) {

        // if we don't fetch the data yet, or we're forcing the reload,
        // or the filter has change we need to fetch the data again
        if( !_data.length || force_reload || _filter_change ) {
            amplify.request(resource_name, _filters, function(data) {
                _filter_change = false
                _data = data
                amplify.publish(storeName + '.change', data)
            })
        }
        return _data
    }

    /** Set or clear a filter **/
    function filter(field, value) {
        if( field === false )
            _filters = {}
        _filter_change = true
        _filters[field] = value
        return this
    }

    getState()

    return {
        getState: getState
        , filter: filter
    }
}

var JobStore = BaseStore("JobStore", "jobs")
var CityStore = BaseStore("CityStore", "cities")