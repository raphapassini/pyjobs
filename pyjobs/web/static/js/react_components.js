var JobsList = React.createClass({displayName: "JobsList",
    getInitialState: function() {
        return {
            data: JobStore.getState(),
        }
    }

    , componentDidMount: function() {
        amplify.subscribe( 'JobStore.change', this._handleChange )
    }

    , componentDidUnmound: function() {
        amplify.unsubscribe( 'JobStore.change', this._handleChange )
    }

    , _handleChange: function(data) {
        this.setState( {data: data} )
    }

    , render: function() {
        var jobs = this.state.data.map( function(job, index) {
            return React.createElement(JobItem, {job: job, key: "job_"+index})
        })
        return(
            React.createElement("div", {className: "row"}, 
                React.createElement("div", {className: "col-md-3 col-sm-12"}, 
                    React.createElement(JobFilter, null)
                ), 
                React.createElement("div", {className: "col-md-9 col-sm-12"}, 
                    jobs
                )
            )
        )
    }
});

var JobItem = React.createClass({displayName: "JobItem",
    render: function() {
        var state_city = ''
        var job = this.props.job

        if( job.state || job.city )
            state_city = React.createElement("span", {className: "pull-right text-uppercase"}, React.createElement("small", null, job.city, "/", job.state))

        return (
            React.createElement("div", {className: "panel panel-default"}, 
                React.createElement("div", {className: "panel-heading"}, 
                    job.title, 
                    state_city
                ), 
                React.createElement("div", {className: "panel-body"}, 
                    job.desc, 
                    React.createElement("br", null), 
                    React.createElement("strong", null, "Pagamento: ", job.pay)
                ), 
                React.createElement("div", {className: "panel-footer"}, 
                    React.createElement("a", {href: config.redirect_url + '?goto=' + encodeURIComponent(job.link), target: "_blank"}, "Ir para a vaga")
                )
            )
        )
    }
})

var JobFilter = React.createClass({displayName: "JobFilter",
    getInitialState: function() {
        return {
            cities: CityStore.getState()
            ,filterCities: []
        }
    }

    , componentDidMount: function() {
        amplify.subscribe( 'CityStore.change', this._handleChange )
    }

    , componentDidUnmound: function() {
        amplify.unsubscribe( 'CityStore.change', this._handleChange )
    }

    , _handleChange: function(data) {
        this.setState( {cities: data} )
    }

    , render: function() {
        var self = this
        var checkboxes = this.state.cities.map(function(city, index) {
            return(
                React.createElement("div", {className: "checkbox", key: "filter_" + city._id}, 
                  React.createElement("label", null, 
                    React.createElement("input", {type: "checkbox", value: city._id, onChange: self._cityFilter.bind(self, city._id)}), 
                    city._id, " (", city.value, ")"
                  )
                )
            )
        })

        return (
            React.createElement("form", null, 
              React.createElement("div", {className: "form-group"}, 
                React.createElement("label", {htmlFor: "cityFilter"}, "Cidades"), 
                checkboxes, 
                React.createElement("button", {className: "btn btn-sm btn-primary", onClick: self._doFilter}, "Filtrar")
              )
            )
        )
    }

    , _cityFilter: function(city, evt) {
        var filterCities = this.state.filterCities.slice()
        var index = filterCities.indexOf(city)

        if( evt.target.checked )
            filterCities.push(city)
        else if( index != -1 )
            filterCities.splice(index, 1)

        this.setState({filterCities: filterCities}, function() {
            JobStore.filter('city__in', filterCities.join())
        })
    }

    , _doFilter: function(evt) {
        evt.preventDefault()
        JobStore.getState()
    }
})