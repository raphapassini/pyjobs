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

    , render: function() {
        var jobs = this.state.data.map( function(job, index) {
            return React.createElement(JobItem, {job: job})
        })
        return(
            React.createElement("div", null, jobs)
        )
    }

    , _handleChange: function(data) {
        this.setState( {data: data} )
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
                    React.createElement("a", {href: config.redirect_url + '?goto=' + urlencode(job.link), target: "_blank"}, "Ir para a vaga")
                )
            )
        )
    }
})