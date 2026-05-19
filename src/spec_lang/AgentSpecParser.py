# Generated from ./src/spec_lang/AgentSpec.g4 by ANTLR 4.13.2
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
        4,1,36,177,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,3,1,46,8,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,
        1,3,3,3,58,8,3,1,3,1,3,1,3,5,3,63,8,3,10,3,12,3,66,9,3,1,4,1,4,1,
        4,1,4,1,4,5,4,73,8,4,10,4,12,4,76,9,4,1,5,1,5,4,5,80,8,5,11,5,12,
        5,81,1,6,1,6,4,6,86,8,6,11,6,12,6,87,1,7,1,7,1,7,3,7,93,8,7,1,7,
        1,7,1,7,1,7,3,7,99,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,110,
        8,9,1,9,1,9,1,9,1,9,5,9,116,8,9,10,9,12,9,119,9,9,1,10,1,10,1,10,
        3,10,124,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,134,8,
        11,10,11,12,11,137,9,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,151,8,13,1,14,1,14,1,14,1,14,1,14,5,14,
        158,8,14,10,14,12,14,161,9,14,1,14,1,14,1,15,1,15,1,15,1,16,4,16,
        169,8,16,11,16,12,16,170,1,16,1,16,1,16,1,16,1,16,0,1,18,17,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,1,1,0,31,32,185,0,37,
        1,0,0,0,2,42,1,0,0,0,4,51,1,0,0,0,6,55,1,0,0,0,8,67,1,0,0,0,10,77,
        1,0,0,0,12,83,1,0,0,0,14,98,1,0,0,0,16,100,1,0,0,0,18,109,1,0,0,
        0,20,123,1,0,0,0,22,125,1,0,0,0,24,141,1,0,0,0,26,150,1,0,0,0,28,
        152,1,0,0,0,30,164,1,0,0,0,32,168,1,0,0,0,34,36,3,2,1,0,35,34,1,
        0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,
        37,1,0,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,43,3,4,2,0,43,45,3,6,3,
        0,44,46,3,8,4,0,45,44,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,
        3,10,5,0,48,49,3,12,6,0,49,50,5,11,0,0,50,3,1,0,0,0,51,52,5,1,0,
        0,52,53,5,21,0,0,53,54,5,29,0,0,54,5,1,0,0,0,55,57,5,2,0,0,56,58,
        5,7,0,0,57,56,1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,64,3,14,7,0,
        60,61,5,24,0,0,61,63,3,14,7,0,62,60,1,0,0,0,63,66,1,0,0,0,64,62,
        1,0,0,0,64,65,1,0,0,0,65,7,1,0,0,0,66,64,1,0,0,0,67,74,5,5,0,0,68,
        69,5,6,0,0,69,70,5,29,0,0,70,71,5,22,0,0,71,73,3,22,11,0,72,68,1,
        0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,9,1,0,0,0,76,
        74,1,0,0,0,77,79,5,3,0,0,78,80,3,26,13,0,79,78,1,0,0,0,80,81,1,0,
        0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,11,1,0,0,0,83,85,5,4,0,0,84,86,
        3,20,10,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,
        0,88,13,1,0,0,0,89,92,5,29,0,0,90,91,5,18,0,0,91,93,5,29,0,0,92,
        90,1,0,0,0,92,93,1,0,0,0,93,99,1,0,0,0,94,99,5,33,0,0,95,99,5,34,
        0,0,96,99,5,35,0,0,97,99,5,36,0,0,98,89,1,0,0,0,98,94,1,0,0,0,98,
        95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,15,1,0,0,0,100,101,5,30,
        0,0,101,102,5,12,0,0,102,103,3,18,9,0,103,17,1,0,0,0,104,105,6,9,
        -1,0,105,110,5,30,0,0,106,110,3,24,12,0,107,110,5,29,0,0,108,110,
        3,22,11,0,109,104,1,0,0,0,109,106,1,0,0,0,109,107,1,0,0,0,109,108,
        1,0,0,0,110,117,1,0,0,0,111,112,10,2,0,0,112,113,5,19,0,0,113,114,
        5,30,0,0,114,116,5,20,0,0,115,111,1,0,0,0,116,119,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,19,1,0,0,0,119,117,1,0,0,0,120,124,5,
        27,0,0,121,124,3,22,11,0,122,124,3,32,16,0,123,120,1,0,0,0,123,121,
        1,0,0,0,123,122,1,0,0,0,124,21,1,0,0,0,125,126,5,26,0,0,126,127,
        5,14,0,0,127,128,5,29,0,0,128,129,5,13,0,0,129,130,5,16,0,0,130,
        135,3,16,8,0,131,132,5,13,0,0,132,134,3,16,8,0,133,131,1,0,0,0,134,
        137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,
        135,1,0,0,0,138,139,5,17,0,0,139,140,5,15,0,0,140,23,1,0,0,0,141,
        142,7,0,0,0,142,25,1,0,0,0,143,151,5,9,0,0,144,151,5,10,0,0,145,
        146,5,23,0,0,146,151,3,26,13,0,147,151,5,25,0,0,148,151,5,29,0,0,
        149,151,3,28,14,0,150,143,1,0,0,0,150,144,1,0,0,0,150,145,1,0,0,
        0,150,147,1,0,0,0,150,148,1,0,0,0,150,149,1,0,0,0,151,27,1,0,0,0,
        152,153,5,29,0,0,153,154,5,14,0,0,154,159,3,18,9,0,155,156,5,13,
        0,0,156,158,3,18,9,0,157,155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,
        0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,163,5,15,
        0,0,163,29,1,0,0,0,164,165,5,29,0,0,165,166,5,12,0,0,166,31,1,0,
        0,0,167,169,3,30,15,0,168,167,1,0,0,0,169,170,1,0,0,0,170,168,1,
        0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,5,29,0,0,173,174,5,
        22,0,0,174,175,3,24,12,0,175,33,1,0,0,0,16,37,45,57,64,74,81,87,
        92,98,109,117,123,135,150,159,170
    ]

class AgentSpecParser ( Parser ):

    grammarFileName = "AgentSpec.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'rule'", "'trigger'", "'check'", "'enforce'", 
                     "'prepare'", "'val'", "'act'", "'any'", "'true'", "'false'", 
                     "'end'", "':'", "','", "'('", "')'", "'{'", "'}'", 
                     "'.'", "'['", "']'", "'@'", "'='", "'!'", "'|'", "<INVALID>", 
                     "'invoke_action'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'state_change'", 
                     "'before_action'", "'after_action'", "'finish'" ]

    symbolicNames = [ "<INVALID>", "RULE", "TRIGGER", "CHECK", "ENFORCE", 
                      "PREPARE", "VAL", "ACT", "ANY", "TRUE", "FALSE", "END", 
                      "COLON", "COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "DOT", "LBRACK", "RBRACK", "AT", "EQ", "NOT", "PIPE", 
                      "PREDICATE", "INVOKE", "ENFORCEMENT", "WS", "IDENTIFIER", 
                      "STRING", "INTEGER", "FLOAT", "STATE_CHANGE", "BEFORE_ACTION", 
                      "AFTER_ACTION", "FINISH" ]

    RULE_program = 0
    RULE_rule = 1
    RULE_ruleClause = 2
    RULE_triggerClause = 3
    RULE_prepareClause = 4
    RULE_checkClause = 5
    RULE_enforceClause = 6
    RULE_event = 7
    RULE_kvPair = 8
    RULE_value = 9
    RULE_enforcement = 10
    RULE_actionInvoke = 11
    RULE_number = 12
    RULE_predicate = 13
    RULE_predicate_func = 14
    RULE_namespace = 15
    RULE_config = 16

    ruleNames =  [ "program", "rule", "ruleClause", "triggerClause", "prepareClause", 
                   "checkClause", "enforceClause", "event", "kvPair", "value", 
                   "enforcement", "actionInvoke", "number", "predicate", 
                   "predicate_func", "namespace", "config" ]

    EOF = Token.EOF
    RULE=1
    TRIGGER=2
    CHECK=3
    ENFORCE=4
    PREPARE=5
    VAL=6
    ACT=7
    ANY=8
    TRUE=9
    FALSE=10
    END=11
    COLON=12
    COMMA=13
    LPAREN=14
    RPAREN=15
    LBRACE=16
    RBRACE=17
    DOT=18
    LBRACK=19
    RBRACK=20
    AT=21
    EQ=22
    NOT=23
    PIPE=24
    PREDICATE=25
    INVOKE=26
    ENFORCEMENT=27
    WS=28
    IDENTIFIER=29
    STRING=30
    INTEGER=31
    FLOAT=32
    STATE_CHANGE=33
    BEFORE_ACTION=34
    AFTER_ACTION=35
    FINISH=36

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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 34
                self.rule_()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
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

        def prepareClause(self):
            return self.getTypedRuleContext(AgentSpecParser.PrepareClauseContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.ruleClause()
            self.state = 43
            self.triggerClause()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 44
                self.prepareClause()


            self.state = 47
            self.checkClause()
            self.state = 48
            self.enforceClause()
            self.state = 49
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
            self.state = 51
            self.match(AgentSpecParser.RULE)
            self.state = 52
            self.match(AgentSpecParser.AT)
            self.state = 53
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

        def event(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentSpecParser.EventContext)
            else:
                return self.getTypedRuleContext(AgentSpecParser.EventContext,i)


        def ACT(self):
            return self.getToken(AgentSpecParser.ACT, 0)

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(AgentSpecParser.PIPE)
            else:
                return self.getToken(AgentSpecParser.PIPE, i)

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
            self.state = 55
            self.match(AgentSpecParser.TRIGGER)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 56
                self.match(AgentSpecParser.ACT)


            self.state = 59
            self.event()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 60
                self.match(AgentSpecParser.PIPE)
                self.state = 61
                self.event()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrepareClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREPARE(self):
            return self.getToken(AgentSpecParser.PREPARE, 0)

        def VAL(self, i:int=None):
            if i is None:
                return self.getTokens(AgentSpecParser.VAL)
            else:
                return self.getToken(AgentSpecParser.VAL, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(AgentSpecParser.IDENTIFIER)
            else:
                return self.getToken(AgentSpecParser.IDENTIFIER, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(AgentSpecParser.EQ)
            else:
                return self.getToken(AgentSpecParser.EQ, i)

        def actionInvoke(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentSpecParser.ActionInvokeContext)
            else:
                return self.getTypedRuleContext(AgentSpecParser.ActionInvokeContext,i)


        def getRuleIndex(self):
            return AgentSpecParser.RULE_prepareClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrepareClause" ):
                listener.enterPrepareClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrepareClause" ):
                listener.exitPrepareClause(self)




    def prepareClause(self):

        localctx = AgentSpecParser.PrepareClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_prepareClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(AgentSpecParser.PREPARE)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 68
                self.match(AgentSpecParser.VAL)
                self.state = 69
                self.match(AgentSpecParser.IDENTIFIER)
                self.state = 70
                self.match(AgentSpecParser.EQ)
                self.state = 71
                self.actionInvoke()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 10, self.RULE_checkClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(AgentSpecParser.CHECK)
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.predicate()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 578815488) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_enforceClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(AgentSpecParser.ENFORCE)
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.enforcement()
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 738197504) != 0)):
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(AgentSpecParser.IDENTIFIER)
            else:
                return self.getToken(AgentSpecParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(AgentSpecParser.DOT, 0)

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
        self.enterRule(localctx, 14, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(AgentSpecParser.IDENTIFIER)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 90
                    self.match(AgentSpecParser.DOT)
                    self.state = 91
                    self.match(AgentSpecParser.IDENTIFIER)


                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(AgentSpecParser.STATE_CHANGE)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.match(AgentSpecParser.BEFORE_ACTION)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.match(AgentSpecParser.AFTER_ACTION)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 5)
                self.state = 97
                self.match(AgentSpecParser.FINISH)
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
        self.enterRule(localctx, 16, self.RULE_kvPair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(AgentSpecParser.STRING)
            self.state = 101
            self.match(AgentSpecParser.COLON)
            self.state = 102
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_value, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.state = 105
                self.match(AgentSpecParser.STRING)
                pass
            elif token in [31, 32]:
                self.state = 106
                self.number()
                pass
            elif token in [29]:
                self.state = 107
                self.match(AgentSpecParser.IDENTIFIER)
                pass
            elif token in [26]:
                self.state = 108
                self.actionInvoke()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AgentSpecParser.ValueContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_value)
                    self.state = 111
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 112
                    self.match(AgentSpecParser.LBRACK)
                    self.state = 113
                    self.match(AgentSpecParser.STRING)
                    self.state = 114
                    self.match(AgentSpecParser.RBRACK) 
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_enforcement)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(AgentSpecParser.ENFORCEMENT)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.actionInvoke()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
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

        def LBRACE(self):
            return self.getToken(AgentSpecParser.LBRACE, 0)

        def kvPair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentSpecParser.KvPairContext)
            else:
                return self.getTypedRuleContext(AgentSpecParser.KvPairContext,i)


        def RBRACE(self):
            return self.getToken(AgentSpecParser.RBRACE, 0)

        def RPAREN(self):
            return self.getToken(AgentSpecParser.RPAREN, 0)

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
        self.enterRule(localctx, 22, self.RULE_actionInvoke)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(AgentSpecParser.INVOKE)
            self.state = 126
            self.match(AgentSpecParser.LPAREN)
            self.state = 127
            self.match(AgentSpecParser.IDENTIFIER)
            self.state = 128
            self.match(AgentSpecParser.COMMA)
            self.state = 129
            self.match(AgentSpecParser.LBRACE)
            self.state = 130
            self.kvPair()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 131
                self.match(AgentSpecParser.COMMA)
                self.state = 132
                self.kvPair()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(AgentSpecParser.RBRACE)
            self.state = 139
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
        self.enterRule(localctx, 24, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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

        def IDENTIFIER(self):
            return self.getToken(AgentSpecParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 26, self.RULE_predicate)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(AgentSpecParser.TRUE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(AgentSpecParser.FALSE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.match(AgentSpecParser.NOT)
                self.state = 146
                self.predicate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.match(AgentSpecParser.PREDICATE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
                self.match(AgentSpecParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 149
                self.predicate_func()
                pass


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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentSpecParser.ValueContext)
            else:
                return self.getTypedRuleContext(AgentSpecParser.ValueContext,i)


        def RPAREN(self):
            return self.getToken(AgentSpecParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentSpecParser.COMMA)
            else:
                return self.getToken(AgentSpecParser.COMMA, i)

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
        self.enterRule(localctx, 28, self.RULE_predicate_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(AgentSpecParser.IDENTIFIER)
            self.state = 153
            self.match(AgentSpecParser.LPAREN)
            self.state = 154
            self.value(0)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 155
                self.match(AgentSpecParser.COMMA)
                self.state = 156
                self.value(0)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
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
        self.enterRule(localctx, 30, self.RULE_namespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(AgentSpecParser.IDENTIFIER)
            self.state = 165
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
        self.enterRule(localctx, 32, self.RULE_config)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 167
                    self.namespace()

                else:
                    raise NoViableAltException(self)
                self.state = 170 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 172
            self.match(AgentSpecParser.IDENTIFIER)
            self.state = 173
            self.match(AgentSpecParser.EQ)
            self.state = 174
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
        self._predicates[9] = self.value_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def value_sempred(self, localctx:ValueContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




