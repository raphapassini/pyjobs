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
        var jobs = this.state.data.map(function(job, index) {
            return React.createElement(JobItem, {key: 'job_' + job.uid, job: job})
        })

        job = {}

        return (
            {jobs}
        );
    }

    , _handleChange: function(data) {
        this.setState({data: data})
    }
});

var JobItem = React.createClass({displayName: "JobItem",
    render: function() {
        return (
            React.createElement("div", {className: "panel panel-default"}, 
                React.createElement("div", {className: "panel-heading"}, this.props.job.title), 
                React.createElement("div", {className: "panel-body"}, 
                    this.props.job.desc
                )
            )
        )
    }
})