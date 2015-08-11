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
        this.state.data.map(function(i, e) {
            console.log(i, e)
        })

        job = {}

        return (
            React.createElement(JobItem, {job: job})
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