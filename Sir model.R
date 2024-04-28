# Setup -------------------------------------------------------------------

rm(list = ls())

library(ggplot2)
library(tibble)

# Variables ---------------------------------------------------------------

pop = 1000
days =360
time_infection = 21

# Iniciliza a matriz
m.pop = matrix(-1, nrow=days, ncol = pop)

# Inicializa a primeira pessoa infectada
# 0 = Imune
# 21~1 : dias doentes
#  -1 = sucetivel
# m.pop[1,1] = time_infection

i=2
for(i in 1:days){
  
  Total_infectado = sum( m.pop[i-1, ] > 0)
  Total_sucetivel = sum( m.pop[i-1, ] < 0)
  
  v_select_infectados = m.pop[i-1, ] > 0
  v_select_imunes = m.pop[i-1,]==0
  
  # Para os que estao infectados, reduzir um dia a infecao
  m.pop[i, v_select_infectados] = m.pop[i-1, v_select_infectados] -1
  
  # Para os que estao imunes, continuar imunes
  m.pop[i, v_select_imunes]=0
  
  # Para os que nao estao imunes, nem infectados avaliar: (1) Se encontram
  # alguem infectados; (2) Se encontrarem alguem infectado se eles se contaminam
  v_will_find_infected = runif(n=pop) > (1/(Total_infectado+2))
  v_will_be_contaminated = runif(n = pop) < 0.013
  
  m.pop[i, v_will_find_infected & !v_select_infectados & !v_select_imunes & v_will_be_contaminated]=time_infection
  
}



# Function ----------------------------------------------------------------

total.infected=function (x){
  return(sum(x>0))
}
total.imune=function (x){
  return(sum(x==0))
}

# Data --------------------------------------------------------------------

tbl <- tibble(day = seq_len(nrow(m.pop)),
              TotalInfected = apply(m.pop, 1, total.infected),
              TotalImune = apply(m.pop, 1, total.imune))

ggplot(tbl) + 
  geom_line(aes(x = day, y = TotalInfected, colour="Infected")) + 
  geom_line(aes(x = day, y = TotalImune, colour="Imune")) + 
  geom_hline(yintercept = 0.3*pop, color= "blue", linetype = "dashed") +
  ylim(0, pop) + 
  theme_bw() +
  theme(legend.position = "bottom") +
  labs(y = NULL, x = NULL, colour = NULL)

