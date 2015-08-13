var JobsList = React.createClass({
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
            return <JobItem job={job} key={"job_"+index} />
        })
        return(
            <div className="row">
                <div className="col-md-3 col-sm-12">
                    <JobFilter />
                </div>
                <div className="col-md-9 col-sm-12">
                    {jobs}
                </div>
            </div>
        )
    }
});

var JobItem = React.createClass({
    render: function() {
        var state_city = ''
        var job = this.props.job

        if( job.state || job.city )
            state_city = <span className="pull-right text-uppercase"><small>{job.city}/{job.state}</small></span>

        return (
            <div className="panel panel-default">
                <div className="panel-heading">
                    {job.title}
                    {state_city}
                </div>
                <div className="panel-body">
                    {job.desc}
                    <br/>
                    <strong>Pagamento: {job.pay}</strong>
                </div>
                <div className="panel-footer">
                    <a href={config.redirect_url + '?goto=' + encodeURIComponent(job.link) } target="_blank">Ir para a vaga</a>
                </div>
            </div>
        )
    }
})

var JobFilter = React.createClass({
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
                <div className="checkbox" key={"filter_" + city._id} >
                  <label>
                    <input type="checkbox" value={city._id} onChange={self._cityFilter.bind(self, city._id)} />
                    {city._id} ({city.value})
                  </label>
                </div>
            )
        })

        return (
            <form>
              <div className="form-group">
                <label htmlFor="cityFilter">Cidades</label>
                {checkboxes}
                <button className="btn btn-sm btn-primary" onClick={self._doFilter}>Filtrar</button>
              </div>
            </form>
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