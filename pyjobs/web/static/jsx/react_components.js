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

    , render: function() {
        var jobs = this.state.data.map( function(job, index) {
            return <JobItem job={job} />
        })
        return(
            <div>{jobs}</div>
        )
    }

    , _handleChange: function(data) {
        this.setState( {data: data} )
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