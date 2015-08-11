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
            state_city = React.createElement("span", {className: "pull-right"}, job.state, "/", job.city)

        return (
            React.createElement("div", {className: "panel panel-default"}, 
                React.createElement("div", {className: "panel-heading"}, 
                    this.props.job.title, 
                    state_city
                ), 
                React.createElement("div", {className: "panel-body"}, 
                    this.props.job.desc, 
                    React.createElement("br", null), 
                    React.createElement("a", {href: this.props.job.link, target: "_blank"}, "Ir para a vaga")
                )
            )
        )
    }
})