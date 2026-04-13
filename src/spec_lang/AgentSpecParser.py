# Generated from AgentSpec.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,143,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,3,3,53,8,3,1,3,1,3,1,
        4,1,4,4,4,59,8,4,11,4,12,4,60,1,5,1,5,4,5,65,8,5,11,5,12,5,66,1,
        6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,80,8,8,1,8,1,8,1,8,
        1,8,5,8,86,8,8,10,8,12,8,89,9,8,1,9,1,9,1,9,3,9,94,8,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,105,8,10,10,10,12,10,108,
        9,10,1,10,1,10,3,10,112,8,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,3,12,124,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,15,4,15,135,8,15,11,15,12,15,136,1,15,1,15,1,15,1,15,1,15,
        0,1,16,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,2,0,26,
        26,30,33,1,0,28,29,143,0,35,1,0,0,0,2,40,1,0,0,0,4,46,1,0,0,0,6,
        50,1,0,0,0,8,56,1,0,0,0,10,62,1,0,0,0,12,68,1,0,0,0,14,70,1,0,0,
        0,16,79,1,0,0,0,18,93,1,0,0,0,20,95,1,0,0,0,22,115,1,0,0,0,24,123,
        1,0,0,0,26,125,1,0,0,0,28,130,1,0,0,0,30,134,1,0,0,0,32,34,3,2,1,
        0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,
        1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,41,3,4,2,0,41,
        42,3,6,3,0,42,43,3,8,4,0,43,44,3,10,5,0,44,45,5,9,0,0,45,3,1,0,0,
        0,46,47,5,1,0,0,47,48,5,19,0,0,48,49,5,26,0,0,49,5,1,0,0,0,50,52,
        5,2,0,0,51,53,5,3,0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,
        54,55,3,12,6,0,55,7,1,0,0,0,56,58,5,4,0,0,57,59,3,24,12,0,58,57,
        1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,9,1,0,0,0,62,
        64,5,5,0,0,63,65,3,18,9,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,
        0,0,66,67,1,0,0,0,67,11,1,0,0,0,68,69,7,0,0,0,69,13,1,0,0,0,70,71,
        5,27,0,0,71,72,5,10,0,0,72,73,3,16,8,0,73,15,1,0,0,0,74,75,6,8,-1,
        0,75,80,5,27,0,0,76,80,3,22,11,0,77,80,5,26,0,0,78,80,3,20,10,0,
        79,74,1,0,0,0,79,76,1,0,0,0,79,77,1,0,0,0,79,78,1,0,0,0,80,87,1,
        0,0,0,81,82,10,2,0,0,82,83,5,17,0,0,83,84,5,27,0,0,84,86,5,18,0,
        0,85,81,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,17,
        1,0,0,0,89,87,1,0,0,0,90,94,5,24,0,0,91,94,3,20,10,0,92,94,3,30,
        15,0,93,90,1,0,0,0,93,91,1,0,0,0,93,92,1,0,0,0,94,19,1,0,0,0,95,
        96,5,23,0,0,96,97,5,12,0,0,97,98,5,26,0,0,98,111,5,11,0,0,99,112,
        3,16,8,0,100,101,5,14,0,0,101,106,3,14,7,0,102,103,5,11,0,0,103,
        105,3,14,7,0,104,102,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,
        107,1,0,0,0,107,109,1,0,0,0,108,106,1,0,0,0,109,110,5,15,0,0,110,
        112,1,0,0,0,111,99,1,0,0,0,111,100,1,0,0,0,112,113,1,0,0,0,113,114,
        5,13,0,0,114,21,1,0,0,0,115,116,7,1,0,0,116,23,1,0,0,0,117,124,5,
        7,0,0,118,124,5,8,0,0,119,120,5,21,0,0,120,124,3,24,12,0,121,124,
        5,22,0,0,122,124,3,26,13,0,123,117,1,0,0,0,123,118,1,0,0,0,123,119,
        1,0,0,0,123,121,1,0,0,0,123,122,1,0,0,0,124,25,1,0,0,0,125,126,5,
        26,0,0,126,127,5,12,0,0,127,128,3,22,11,0,128,129,5,13,0,0,129,27,
        1,0,0,0,130,131,5,26,0,0,131,132,5,10,0,0,132,29,1,0,0,0,133,135,
        3,28,14,0,134,133,1,0,0,0,135,136,1,0,0,0,136,134,1,0,0,0,136,137,
        1,0,0,0,137,138,1,0,0,0,138,139,5,26,0,0,139,140,5,20,0,0,140,141,
        3,22,11,0,141,31,1,0,0,0,11,35,52,60,66,79,87,93,106,111,123,136
    ]

class AgentSpecParser ( Parser ):

    grammarFileName = "AgentSpec.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'rule'", "'trigger'", "'act'", "'check'", 
                     "'enforce'", "'any'", "'true'", "'false'", "'end'", 
                     "':'", "','", "'('", "')'", "'{'", "'}'", "'.'", "'['", 
                     "']'", "'@'", "'='", "'!'", "<INVALID>", "'invoke_action'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'state_change'", "'before_action'", 
                     "'after_action'", "'finish'" ]

    symbolicNames = [ "<INVALID>", "RULE", "TRIGGER", "ACT", "CHECK", "ENFORCE", 
                      "ANY", "TRUE", "FALSE", "END", "COLON", "COMMA", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "DOT", "LBRACK", "RBRACK", 
                      "AT", "EQ", "NOT", "PREDICATE", "INVOKE", "ENFORCEMENT", 
                      "WS", "IDENTIFIER", "STRING", "INTEGER", "FLOAT", 
                      "STATE_CHANGE", "BEFORE_ACTION", "AFTER_ACTION", "FINISH" ]

    RULE_program = 0
    RULE_rule = 1
    RULE_ruleClause = 2
    RULE_triggerClause = 3
    RULE_checkClause = 4
    RULE_enforceClause = 5
    RULE_event = 6
    RULE_kvPair = 7
    RULE_value = 8
    RULE_enforcement = 9
    RULE_actionInvoke = 10
    RULE_number = 11
    RULE_predicate = 12
    RULE_predicate_func = 13
    RULE_namespace = 14
    RULE_config = 15

    ruleNames =  [ "program", "rule", "ruleClause", "triggerClause", "checkClause", 
                   "enforceClause", "event", "kvPair", "value", "enforcement", 
                   "actionInvoke", "number", "predicate", "predicate_func", 
                   "namespace", "config" ]

    EOF = Token.EOF
    RULE=1
    TRIGGER=2
    ACT=3
    CHECK=4
    ENFORCE=5
    ANY=6
    TRUE=7
    FALSE=8
    END=9
    COLON=10
    COMMA=11
    LPAREN=12
    RPAREN=13
    LBRACE=14
    RBRACE=15
    DOT=16
    LBRACK=17
    RBRACK=18
    AT=19
    EQ=20
    NOT=21
    PREDICATE=22
    INVOKE=23
    ENFORCEMENT=24
    WS=25
    IDENTIFIER=26
    STRING=27
    INTEGER=28
    FLOAT=29
    STATE_CHANGE=30
    BEFORE_ACTION=31
    AFTER_ACTION=32
    FINISH=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AgentSpecParser.EOF, 0)

        def rule_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentSpecParser.RuleContext)
            else:
                return self.getTypedRuleContext(AgentSpecParser.RuleContext,i)


        def getRuleIndex(self):
            return AgentSpecParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = AgentSpecParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 32
                self.rule_()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(AgentSpecParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruleClause(self):
            return self.getTypedRuleContext(AgentSpecParser.RuleClauseContext,0)


        def triggerClause(self):
            return self.getTypedRuleContext(AgentSpecParser.TriggerClauseContext,0)


        def checkClause(self):
            return self.getTypedRuleContext(AgentSpecParser.CheckClauseContext,0)


        def enforceClause(self):
            return self.getTypedRuleContext(AgentSpecParser.EnforceClauseContext,0)


        def END(self):
            return self.getToken(AgentSpecParser.END, 0)

        def getRuleIndex(self):
            return AgentSpecParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)




    def rule_(self):

        localctx = AgentSpecParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.ruleClause()
            self.state = 41
            self.triggerClause()
            self.state = 42
            self.checkClause()
            self.state = 43
            self.enforceClause()
            self.state = 44
            self.match(AgentSpecParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE(self):
            return self.getToken(AgentSpecParser.RULE, 0)

        def AT(self):
            return self.getToken(AgentSpecParser.AT, 0)

        def IDENTIFIER(self):
            return self.getToken(AgentSpecParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return AgentSpecParser.RULE_ruleClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleClause" ):
                listener.enterRuleClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleClause" ):
                listener.exitRuleClause(self)




    def ruleClause(self):

        localctx = AgentSpecParser.RuleClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ruleClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(AgentSpecParser.RULE)
            self.state = 47
            self.match(AgentSpecParser.AT)
            self.state = 48
            self.match(AgentSpecParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TriggerClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRIGGER(self):
            return self.getToken(AgentSpecParser.TRIGGER, 0)

        def event(self):
            return self.getTypedRuleContext(AgentSpecParser.EventContext,0)


        def ACT(self):
            return self.getToken(AgentSpecParser.ACT, 0)

        def getRuleIndex(self):
            return AgentSpecParser.RULE_triggerClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTriggerClause" ):
                listener.enterTriggerClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTriggerClause" ):
                listener.exitTriggerClause(self)




    def triggerClause(self):

        localctx = AgentSpecParser.TriggerClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_triggerClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(AgentSpecParser.TRIGGER)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 51
                self.match(AgentSpecParser.ACT)


            self.state = 54
            self.event()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CheckClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHECK(self):
            return self.getToken(AgentSpecParser.CHECK, 0)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentSpecParser.PredicateContext)
            else:
                return self.getTypedRuleContext(AgentSpecParser.PredicateContext,i)


        def getRuleIndex(self):
            return AgentSpecParser.RULE_checkClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheckClause" ):
                listener.enterCheckClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheckClause" ):
                listener.exitCheckClause(self)




    def checkClause(self):

        localctx = AgentSpecParser.CheckClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_checkClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(AgentSpecParser.CHECK)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.predicate()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 73400704) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnforceClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENFORCE(self):
            return self.getToken(AgentSpecParser.ENFORCE, 0)

        def enforcement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentSpecParser.EnforcementContext)
            else:
                return self.getTypedRuleContext(AgentSpecParser.EnforcementContext,i)


        def getRuleIndex(self):
            return AgentSpecParser.RULE_enforceClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnforceClause" ):
                listener.enterEnforceClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnforceClause" ):
                listener.exitEnforceClause(self)




    def enforceClause(self):

        localctx = AgentSpecParser.EnforceClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_enforceClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(AgentSpecParser.ENFORCE)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.enforcement()
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 92274688) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AgentSpecParser.IDENTIFIER, 0)

        def STATE_CHANGE(self):
            return self.getToken(AgentSpecParser.STATE_CHANGE, 0)

        def BEFORE_ACTION(self):
            return self.getToken(AgentSpecParser.BEFORE_ACTION, 0)

        def AFTER_ACTION(self):
            return self.getToken(AgentSpecParser.AFTER_ACTION, 0)

        def FINISH(self):
            return self.getToken(AgentSpecParser.FINISH, 0)

        def getRuleIndex(self):
            return AgentSpecParser.RULE_event

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent" ):
                listener.enterEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent" ):
                listener.exitEvent(self)




    def event(self):

        localctx = AgentSpecParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16173236224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KvPairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AgentSpecParser.STRING, 0)

        def COLON(self):
            return self.getToken(AgentSpecParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(AgentSpecParser.ValueContext,0)


        def getRuleIndex(self):
            return AgentSpecParser.RULE_kvPair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKvPair" ):
                listener.enterKvPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKvPair" ):
                listener.exitKvPair(self)




    def kvPair(self):

        localctx = AgentSpecParser.KvPairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_kvPair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(AgentSpecParser.STRING)
            self.state = 71
            self.match(AgentSpecParser.COLON)
            self.state = 72
            self.value(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AgentSpecParser.STRING, 0)

        def number(self):
            return self.getTypedRuleContext(AgentSpecParser.NumberContext,0)


        def IDENTIFIER(self):
            return self.getToken(AgentSpecParser.IDENTIFIER, 0)

        def actionInvoke(self):
            return self.getTypedRuleContext(AgentSpecParser.ActionInvokeContext,0)


        def value(self):
            return self.getTypedRuleContext(AgentSpecParser.ValueContext,0)


        def LBRACK(self):
            return self.getToken(AgentSpecParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(AgentSpecParser.RBRACK, 0)

        def getRuleIndex(self):
            return AgentSpecParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)



    def value(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AgentSpecParser.ValueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_value, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 75
                self.match(AgentSpecParser.STRING)
                pass
            elif token in [28, 29]:
                self.state = 76
                self.number()
                pass
            elif token in [26]:
                self.state = 77
                self.match(AgentSpecParser.IDENTIFIER)
                pass
            elif token in [23]:
                self.state = 78
                self.actionInvoke()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AgentSpecParser.ValueContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_value)
                    self.state = 81
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 82
                    self.match(AgentSpecParser.LBRACK)
                    self.state = 83
                    self.match(AgentSpecParser.STRING)
                    self.state = 84
                    self.match(AgentSpecParser.RBRACK) 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EnforcementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENFORCEMENT(self):
            return self.getToken(AgentSpecParser.ENFORCEMENT, 0)

        def actionInvoke(self):
            return self.getTypedRuleContext(AgentSpecParser.ActionInvokeContext,0)


        def config(self):
            return self.getTypedRuleContext(AgentSpecParser.ConfigContext,0)


        def getRuleIndex(self):
            return AgentSpecParser.RULE_enforcement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnforcement" ):
                listener.enterEnforcement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnforcement" ):
                listener.exitEnforcement(self)




    def enforcement(self):

        localctx = AgentSpecParser.EnforcementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_enforcement)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(AgentSpecParser.ENFORCEMENT)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.actionInvoke()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.config()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionInvokeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INVOKE(self):
            return self.getToken(AgentSpecParser.INVOKE, 0)

        def LPAREN(self):
            return self.getToken(AgentSpecParser.LPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(AgentSpecParser.IDENTIFIER, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentSpecParser.COMMA)
            else:
                return self.getToken(AgentSpecParser.COMMA, i)

        def RPAREN(self):
            return self.getToken(AgentSpecParser.RPAREN, 0)

        def value(self):
            return self.getTypedRuleContext(AgentSpecParser.ValueContext,0)


        def LBRACE(self):
            return self.getToken(AgentSpecParser.LBRACE, 0)

        def kvPair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentSpecParser.KvPairContext)
            else:
                return self.getTypedRuleContext(AgentSpecParser.KvPairContext,i)


        def RBRACE(self):
            return self.getToken(AgentSpecParser.RBRACE, 0)

        def getRuleIndex(self):
            return AgentSpecParser.RULE_actionInvoke

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionInvoke" ):
                listener.enterActionInvoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionInvoke" ):
                listener.exitActionInvoke(self)




    def actionInvoke(self):

        localctx = AgentSpecParser.ActionInvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_actionInvoke)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(AgentSpecParser.INVOKE)
            self.state = 96
            self.match(AgentSpecParser.LPAREN)
            self.state = 97
            self.match(AgentSpecParser.IDENTIFIER)
            self.state = 98
            self.match(AgentSpecParser.COMMA)
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 26, 27, 28, 29]:
                self.state = 99
                self.value(0)
                pass
            elif token in [14]:
                self.state = 100
                self.match(AgentSpecParser.LBRACE)
                self.state = 101
                self.kvPair()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 102
                    self.match(AgentSpecParser.COMMA)
                    self.state = 103
                    self.kvPair()
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 109
                self.match(AgentSpecParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 113
            self.match(AgentSpecParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(AgentSpecParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(AgentSpecParser.FLOAT, 0)

        def getRuleIndex(self):
            return AgentSpecParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = AgentSpecParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(AgentSpecParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(AgentSpecParser.FALSE, 0)

        def NOT(self):
            return self.getToken(AgentSpecParser.NOT, 0)

        def predicate(self):
            return self.getTypedRuleContext(AgentSpecParser.PredicateContext,0)


        def PREDICATE(self):
            return self.getToken(AgentSpecParser.PREDICATE, 0)

        def predicate_func(self):
            return self.getTypedRuleContext(AgentSpecParser.Predicate_funcContext,0)


        def getRuleIndex(self):
            return AgentSpecParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = AgentSpecParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_predicate)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(AgentSpecParser.TRUE)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(AgentSpecParser.FALSE)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(AgentSpecParser.NOT)
                self.state = 120
                self.predicate()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.match(AgentSpecParser.PREDICATE)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 122
                self.predicate_func()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predicate_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AgentSpecParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(AgentSpecParser.LPAREN, 0)

        def number(self):
            return self.getTypedRuleContext(AgentSpecParser.NumberContext,0)


        def RPAREN(self):
            return self.getToken(AgentSpecParser.RPAREN, 0)

        def getRuleIndex(self):
            return AgentSpecParser.RULE_predicate_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate_func" ):
                listener.enterPredicate_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate_func" ):
                listener.exitPredicate_func(self)




    def predicate_func(self):

        localctx = AgentSpecParser.Predicate_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_predicate_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(AgentSpecParser.IDENTIFIER)
            self.state = 126
            self.match(AgentSpecParser.LPAREN)
            self.state = 127
            self.number()
            self.state = 128
            self.match(AgentSpecParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AgentSpecParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(AgentSpecParser.COLON, 0)

        def getRuleIndex(self):
            return AgentSpecParser.RULE_namespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace" ):
                listener.enterNamespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace" ):
                listener.exitNamespace(self)




    def namespace(self):

        localctx = AgentSpecParser.NamespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_namespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(AgentSpecParser.IDENTIFIER)
            self.state = 131
            self.match(AgentSpecParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AgentSpecParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(AgentSpecParser.EQ, 0)

        def number(self):
            return self.getTypedRuleContext(AgentSpecParser.NumberContext,0)


        def namespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentSpecParser.NamespaceContext)
            else:
                return self.getTypedRuleContext(AgentSpecParser.NamespaceContext,i)


        def getRuleIndex(self):
            return AgentSpecParser.RULE_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig" ):
                listener.enterConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig" ):
                listener.exitConfig(self)




    def config(self):

        localctx = AgentSpecParser.ConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_config)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 133
                    self.namespace()

                else:
                    raise NoViableAltException(self)
                self.state = 136 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 138
            self.match(AgentSpecParser.IDENTIFIER)
            self.state = 139
            self.match(AgentSpecParser.EQ)
            self.state = 140
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.value_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def value_sempred(self, localctx:ValueContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




