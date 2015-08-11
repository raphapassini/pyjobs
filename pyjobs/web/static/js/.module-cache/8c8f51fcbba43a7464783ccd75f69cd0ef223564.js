var JobsList = React.createClass({displayName: "JobsList",
    render: function() {
        return (
            React.createElement("div", {className: "panel panel-default"}, 
                React.createElement("div", {className: "panel-heading"}, "Panel heading without title"), 
                React.createElement("div", {className: "panel-body"}, 
                    "Panel content"
                )
            )
        );
    }
});