
grammar AgentSpec;

// Lexer Rules
RULE: 'rule';
TRIGGER: 'trigger';
CHECK: 'check';
ENFORCE: 'enforce';
PREPARE: 'prepare';
VAL: 'val';
ACT: 'act';
ANY: 'any'; 
TRUE: 'true';
FALSE: 'false'; 
END: 'end';
COLON: ':'; 
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
DOT: '.';
LBRACK: '[';
RBRACK: ']';
AT: '@';    
EQ: '=';
NOT: '!';
PIPE: '|';
PREDICATE: 'involve_system_file' | 'submit_post_request' | 'write_to_io' | 'request_untrusted_source' | 'copy_file' | 'involve_system_dir' | 'list_directory' | 'encode_data' | 'read_io' | 'destuctive_os_inst' | 'involve_bash_rc' | 'execute_script' | 'predicate11' | 'has_bias_issues' | 'is_buggy_ip_validation_code' | 'is_side_channel_vulnerable' | 'is_improper_execution_privilege_code' | 'is_buggy_process_management' | 'is_prng_buggy' | 'is_crypto_buggy' | 'is_amplification' | 'detect_missing_default_case' | 'detect_flawed_workflow' | 'detect_unsafe_deserialization' | 'detect_duplicate_keys_in_code' | 'is_candle' | 'is_fragile' | 'is_wettable' | 'is_into_microwave' | 'is_holding_none_microwave_objects' | 'is_on_stoveburner' | 'is_none_stoveburner_obj' | 'is_into_fridge' | 'is_none_fridge_obj' | 'is_unsafe_put' | 'is_unsafe_fillliquid' ;
INVOKE: 'invoke_action';
ENFORCEMENT: 'user_inspection' | 'llm_self_reflect' | 'stop' | 'none' | 'skip'; //todo: customized enforcements
WS: [ \t\r\n]+ -> skip; // Ignore whitespace
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*; // Identifier rule
STRING: '"' .*? '"'; // String literal
INTEGER: [0-9]+;                         // Whole numbers
FLOAT: [0-9]+ '.' [0-9]* | '.' [0-9]+;   // Decimal numbers
STATE_CHANGE: 'state_change';
BEFORE_ACTION: 'before_action';
AFTER_ACTION: 'after_action';
FINISH: 'finish'; 

// Parser Rules
program: rule* EOF; 

rule: ruleClause
      triggerClause 
      prepareClause?
      checkClause
      enforceClause
      END;

ruleClause: RULE AT IDENTIFIER;

triggerClause: TRIGGER (ACT)? event (PIPE event)*;

prepareClause: PREPARE (VAL IDENTIFIER EQ actionInvoke)*;

checkClause: CHECK predicate+;

enforceClause: ENFORCE enforcement+; 

event: IDENTIFIER (DOT IDENTIFIER)? | STATE_CHANGE | BEFORE_ACTION | AFTER_ACTION | FINISH;

kvPair: STRING COLON value;

value: STRING | number | IDENTIFIER | value LBRACK STRING RBRACK | actionInvoke;

enforcement: ENFORCEMENT | actionInvoke | config;

actionInvoke: INVOKE LPAREN IDENTIFIER COMMA LBRACE kvPair (COMMA kvPair)* RBRACE RPAREN;
  
number: INTEGER | FLOAT; 

predicate: TRUE | FALSE | NOT predicate | PREDICATE | IDENTIFIER | predicate_func; 

// predicate function: eq(...), llm_judge(...), or general IDENTIFIER(...)
predicate_func: IDENTIFIER LPAREN value (COMMA value)* RPAREN;

namespace: IDENTIFIER COLON;

config: namespace+ IDENTIFIER EQ number;