before = """
<p:timing>
<p:tnLst>
<p:par>
<p:cTn id="1" nodeType="tmRoot" restart="never" dur="indefinite">
<p:childTnLst>
<p:seq nextAc="seek" concurrent="1">
<p:cTn id="2" nodeType="mainSeq" dur="indefinite">
<p:childTnLst>
""".replace("\n", "")

after = """
</p:childTnLst>
</p:cTn>
<p:prevCondLst>
<p:cond delay="0" evt="onPrev">
<p:tgtEl>
<p:sldTgt/>
</p:tgtEl>
</p:cond>
</p:prevCondLst>
<p:nextCondLst>
<p:cond delay="0" evt="onNext">
<p:tgtEl>
<p:sldTgt/>
</p:tgtEl>
</p:cond>
</p:nextCondLst>
</p:seq>
</p:childTnLst>
</p:cTn>
</p:par>
</p:tnLst>
</p:timing>
""".replace("\n", "")

animation = ["""
<p:par>
<p:cTn id="3" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="4" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="5" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="6" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="0" st="0"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
""", """
<p:par>
<p:cTn id="7" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="8" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="9" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="10" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="1" st="1"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
""", """
<p:par>
<p:cTn id="11" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="12" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="13" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="14" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="2" st="2"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
""", """
<p:par>
<p:cTn id="15" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="16" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="17" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="18" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="3" st="3"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
""", """
<p:par>
<p:cTn id="19" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="20" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="21" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="22" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="4" st="4"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
""", """
<p:par>
<p:cTn id="23" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="24" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="25" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="26" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="5" st="5"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
""", """
<p:par>
<p:cTn id="27" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="28" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="29" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="30" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="6" st="6"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
""", """
<p:par>
<p:cTn id="31" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="32" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="33" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="34" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="7" st="7"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
""", """
<p:par>
<p:cTn id="35" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="36" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="37" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="38" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="8" st="8"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
""", """
<p:par>
<p:cTn id="39" fill="hold">
<p:stCondLst>
<p:cond delay="indefinite"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="40" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:par>
<p:cTn id="41" nodeType="clickEffect" fill="hold" presetSubtype="0" presetClass="entr" presetID="1">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="42" dur="1" fill="hold">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="2">
<p:txEl>
<p:pRg end="9" st="9"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
</p:childTnLst>
</p:cTn>
</p:par>
"""
]