Example of a Spring Web Flow XML
================================
```
<?xml version="1.0" encoding="UTF-8"?>
<flow xmlns="http://www.springframework.org/schema/webflow"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/webflow http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd"
    start-state="Page1" parent="parentflow">

    <!-- When the flow is entered, the expressions in this tag will be executed. -->
    <on-start>
        <evaluate expression="page1FlowAction.onFlowStart"/>
        <evaluate expression="page2FlowAction.onFlowStart"/>
    </on-start>
    
    <view-state id="Page1" view="sample/flow/page1flow">
        <on-entry>
            <evaluate expression="page1FlowAction.onEntry" />
        </on-entry>
        <transition on="submit" to="ChooseNextView">
            <evaluate expression="page1FlowAction.onSubmit" />
        </transition>
    </view-state>

    <action-state id="ChooseNextView">
        <evaluate expression="page1FlowAction.shouldExit" />
        <transition on="no" to="Page1" />
        <transition on="yes" to="Page2" />
    </action-state>

    <view-state id="Page2" view="sample/flow/page2flow">
        <on-entry>
            <evaluate expression="page2FlowAction.onEntry" />
        </on-entry>
        <transition on="submit" to="ExitOrRestart">
            <evaluate expression="page2FlowAction.onSubmit" />
        </transition>
    </view-state>

    <action-state id="ExitOrRestart">
        <evaluate expression="page2FlowAction.shouldExit" />
        <transition on="restart" to="Page1" />
        <transition on="redirect" to="redirect" />
        <transition on="end" to="end" />
    </action-state>
    
    <end-state id="redirect" view="externalRedirect:contextRelative:/"/>
    <end-state id="end"/>

</flow>
```

Example of DOT file
===================
```
digraph "sampleflow-flow.xml" {

  // Start state
	"Start" [label="Start", fontname="Helvetica", shape="circle", style="filled", fillcolor="green"];
	"Start" -> "Page1";

	 // view-state (Page1)
	"Page1" [label="Page1", fontname="Helvetica", shape="oval", style="filled", fillcolor="white", width="2", height="1"];
	"Page1" -> "ChooseNextView" [label="submit", fontname="Helvetica"];

	 // action-state (ChooseNextView)
	"ChooseNextView" [label="ChooseNextView", fontname="Helvetica", shape="oval", style="filled", fillcolor="white", width="2", height="1"];
	"ChooseNextView" -> "Page1" [label="no", fontname="Helvetica"];
	"ChooseNextView" -> "Page2" [label="yes", fontname="Helvetica"];

	 // view-state (Page2)
	"Page2" [label="Page2", fontname="Helvetica", shape="oval", style="filled", fillcolor="white", width="2", height="1"];
	"Page2" -> "ExitOrRestart" [label="submit", fontname="Helvetica"];

	 // action-state (ExitOrRestart)
	"ExitOrRestart" [label="ExitOrRestart", fontname="Helvetica", shape="oval", style="filled", fillcolor="white", width="2", height="1"];
	"ExitOrRestart" -> "Page1" [label="restart", fontname="Helvetica"];
	"ExitOrRestart" -> "redirect" [label="redirect", fontname="Helvetica"];
	"ExitOrRestart" -> "end" [label="end", fontname="Helvetica"];

	 // end-state (redirect)
	"redirect" [label="redirect", fontname="Helvetica", shape="oval", style="filled", fillcolor="white", width="2", height="1"];
	"redirect" -> "End"

	 // end-state (end)
	"end" [label="end", fontname="Helvetica", shape="oval", style="filled", fillcolor="white", width="2", height="1"];
	"end" -> "End"

	// End state
	"End" [label="End", fontname="Helvetica", shape="circle", style="filled", fillcolor="red"];
}
```

Example of DOT graph
====================
![sampleflow-flow.png](https://raw.github.com/johnkchiu/Spring-Web-Flow-XML-To-DOT/master/Sample1/sampleflow-flow.png)
